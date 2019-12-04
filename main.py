import glob
import json
import urllib.parse
import myutil

fileio = myutil.FileIO()


def url2json(url:str):
    json_ = json.loads(urllib.parse.unquote(url).split("json=")[1])
    fileio.write(data=json_, path=f"paifu/json/{'-'.join(map(str, json_['log'][0][0][:2]))}.json")


def main():
    (url2json(url=s) for s in fileio.read(path="paifu/txt/2019093001.txt"))



if __name__ == '__main__':
    main()