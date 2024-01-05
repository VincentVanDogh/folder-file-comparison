class Directory:
    dir_name: str
    dir_files: [str]
    dir_sub: [str]

    def __init__(self, dir_name: str, dir_files: [str], dir_sub: [str]):
        self.dir_name = dir_name
        self.dir_files = dir_files
        self.dir_sub = dir_sub

    def __str__(self):
        result = self.dir_name + ': {'
        for file in self.dir_files:
            result += file + ','
        return
