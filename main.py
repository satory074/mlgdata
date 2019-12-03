import glob
import json
import urllib.parse
import myutil


def main():
    fileio = myutil.FileIO()
    for i, s in enumerate(fileio.load(path="paifu/txt/2019093001.txt")):
        json_ = json.loads(urllib.parse.unquote(s).split("json=")[1])
        json.dump(json_, open(f"paifu/json/{'-'.join(map(str, json_['log'][0][0][:2]))}.json", 'w') , ensure_ascii=False)


if __name__ == '__main__':
    main()