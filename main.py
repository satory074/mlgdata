import glob
import json
import urllib.parse
import myutil


def main():
    fileio = myutil.FileIO()
    for i, s in enumerate(fileio.read(path="paifu/txt/2019093001.txt")):
        json_ = json.loads(urllib.parse.unquote(s).split("json=")[1])
        fileio.write(data=json_, path=f"paifu/json/{'-'.join(map(str, json_['log'][0][0][:2]))}.json")


if __name__ == '__main__':
    main()