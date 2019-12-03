from typing import List


class FileIO:
    @staticmethod
    def load(path: str) -> List[str]:
        if type(path) is str:
            with open(path, mode='r') as f:
                return f.readlines()
        if type(path) is json:
            pass

    @staticmethod
    def output(li: List[str], path: str):
        with open(path, mode='w') as f:
            f.writelines(li)

    @staticmethod
    def write(str_: str, path: str):
        with open(path, mode='a') as f:
            print(str_, file=f)