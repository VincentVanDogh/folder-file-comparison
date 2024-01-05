import os
import sys
from line_difference import LineDifference


def compare_dir_content(dir_path_1: str, dir_path_2: str) -> None:
    content_1: [str] = os.listdir(dir_path_1)
    content_2: [str] = os.listdir(dir_path_2)
    for file in content_1:
        comparison: [LineDifference] = compare_files(f'{dir_path_1}/{file}', f'{dir_path_2}/{file}')
        if len(comparison) > 0:
            print(f'The file {file} is not 1:1 in the src-gen and src-gen-expected directory')
            for line in comparison:
                print(line)
                # print(line.get_line_index())
            print()
        else:
            print(f"CORRECT: {file}")


def compare_files(
        file_path_1: str,
        file_path_2: str,
        ignore_whitespaces: bool = False,
        ignore_case_sensitivity: bool = False
) -> [LineDifference]:
    differences: [LineDifference] = []
    arr1 = split_str_by_newlines(read_file(file_path_1))
    arr2 = split_str_by_newlines(read_file(file_path_2))

    if len(arr1) != len(arr2):
        print(f'Files do not match in length for the following paths:\n{file_path_1}\n{file_path_2}')

    max_length: int = len(arr1) if len(arr1) < len(arr2) else len(arr2)
    i = 0

    while i < max_length:
        if arr1[i] != arr2[i]:
            differences.append(LineDifference(i + 1, arr1[i], arr2[i]))
        i += 1

    return differences


def read_file(file_path: str) -> [str]:
    with open(file_path, "r", encoding="utf8") as file:
        return file.read()


def split_str_by_newlines(content: str):
    return content.split("\n")


def print_dirs(dirs: [str]) -> None:
    # TODO: Delete this method
    for d in dirs:
        print(d)


def print_file_differences(diff: [LineDifference]) -> None:
    print(f'LENGTH: {len(diff)}')
    for d in diff:
        print(d)


# Specify whether only child-folders should be displayed or not
if __name__ == "__main__":
    arguments: [str] = sys.argv[1:]
    print(arguments)

