import json
import os
from typing import List


class FileIO:
    @staticmethod
    def read(path: str):
        _, ext = os.path.splitext(path)

        if ext == '.txt':
            with open(path, mode='r') as f:
                return f.readlines()
        if ext == '.json':
            with open(path) as f:
                return json.load(f)

    @staticmethod
    def output(li: List[str], path: str):
        with open(path, mode='w') as f:
            f.writelines(li)

    @staticmethod
    def write(data:str, path:str, mode_:str="w"):
        _, ext = os.path.splitext(path)

        if ext == '.txt':
            with open(path, mode=mode_) as f:
                print(data, file=f)
        if ext == '.json':
            json.dump(data, open(path, 'w') , ensure_ascii=False)
