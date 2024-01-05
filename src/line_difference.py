import re


class LineDifference:
    line_index: int
    line_1: str
    line_2: str

    def __init__(self, line_index: int, line_1: str, line_2: str):
        self.line_index = line_index
        self.line_1 = line_1
        self.line_2 = line_2

    def compute_diff(self, ignore_equals: bool = True) -> str:
        result = ""
        if self.line_1 == self.line_2 and not ignore_equals:
            return f'{self.line_index}: Same'
        if self.line_1 != self.line_2 and self.line_1.split() == self.line_2.split():
            return self._difference_str(
                self.line_index,
                f'{self.display_trailing_whitespaces_per_line(self.line_1, counter=True)}',
                f'{self.display_trailing_whitespaces_per_line(self.line_2, counter=True)}',
                'Trailing whitespaces'
            )
        return result

    def __str__(self):
        return self._difference_str(
            self.line_index,
            self.line_1.replace("\t", r"\t"),
            self.line_2.replace("\t", r"\t")
        )

    def _difference_str(self, index: int, line_1: str, line_2: str, diff_descr: str = None) -> str:
        if diff_descr is not None:
            result = f'{index}: Difference - {diff_descr} {{\n'
        else:
            result = f'{index}: {{\n'
        result += f'{line_1}\n'
        result += f'{line_2}\n'
        result += '}'
        return result

    def display_trailing_whitespaces(self, counter: bool = False) -> str:
        result = f'{self.line_index}: {{\n'
        result += self.display_trailing_whitespaces_per_line(self.line_1, counter=counter)
        result += self.display_trailing_whitespaces_per_line(self.line_2, counter=counter)
        result += '}'
        return result

    def display_trailing_whitespaces_per_line(self, line: str, counter: bool = False) -> (str, str):
        trailing_whitespaces = re.match(r"^(\s*).*?(\s*)$", line)
        start = trailing_whitespaces.group(1)
        end = trailing_whitespaces.group(2)

        if counter:
            start_counter = self._whitespace_counter(start)
            end_counter = self._whitespace_counter(end)
            return f'{start_counter}{line.strip()}{end_counter}'
        else:
            return f'{line.replace("\t", r"\t").replace(" ", r"\s")}'

    def display_line_difference_whitespaces(self, counter: bool = False) -> str:
        result = f'{self.line_index}: {{\n'
        if not counter:
            result += f'{self.line_1.replace("\t", r"\t").replace(" ", r"\s")}\n'
            result += f'{self.line_2.replace("\t", r"\t").replace(" ", r"\s")}\n'
        else:
            result += f'{self._whitespace_counter(self.line_1)}\n'
            result += f'{self._whitespace_counter(self.line_2)}\n'
        result += '}'
        return result

    def _whitespace_counter(self, line: str) -> str:
        tab_counter: int = 0
        space_counter: int = 0
        line_adjusted: str = ""
        i: int = 0
        while i < len(line):
            re_result = re.match(r"\t|\s", line[i])
            if re_result is not None:
                if re_result.group(0) == '\t':
                    tab_counter += 1
                    if i == len(line) - 1:
                        line_adjusted += rf'\t{{{tab_counter}}}'
                else:
                    space_counter += 1
                    if i == len(line) - 1:
                        line_adjusted += rf'\s{{{space_counter}}}'
            else:
                if tab_counter > 0:
                    line_adjusted += rf'\t{{{tab_counter}}}'
                elif space_counter > 0:
                    line_adjusted += rf'\s{{{space_counter}}}'
                line_adjusted += line[i]
                tab_counter = space_counter = 0
            i += 1
        return line_adjusted

    def get_line_index(self):
        return self.line_index
