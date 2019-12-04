import glob
import json
import urllib.parse
import myutil
from typing import List

fileio = myutil.FileIO()


class Player:
    def __init__(self, haipai:List[int], tsumopai:List[int], sutepai:List[int]):
        self.haipai:List[int] = haipai
        self.tsumopai:List[int] = tsumopai
        self.sutepai:List[int] = sutepai

def url2json(url:str):
    json_ = json.loads(urllib.parse.unquote(url).split("json=")[1])
    fileio.write(data=json_, path=f"paifu/json/{'-'.join(map(str, json_['log'][0][0][:2]))}.json")


def main():
    (url2json(url=s) for s in fileio.read(path="paifu/txt/2019093001.txt"))

    for path in glob.glob('paifu/json/*-*.json'):
        print(fileio.read(path=path))
        exit()



if __name__ == '__main__':
    main()