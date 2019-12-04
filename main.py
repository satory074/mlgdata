import glob
import json
import urllib.parse
import myutil
from typing import List

fileio = myutil.FileIO()


class Player:
    def __init__(self, name: str, team: str, haipai: List[int], tsumopai: List[int], sutepai: List[int]):
        self.name: str = name
        self.team: str = team
        self.haipai: List[int] = haipai
        self.tsumopai: List[int] = tsumopai
        self.sutepai: List[int] = sutepai


def url2json(url: str):
    json_ = json.loads(urllib.parse.unquote(url).split('json=')[1])
    log_ = {}
    log_['kyoku'] = {'nkyoku': json_['log'][0][0][0],
                     'nhonba': json_['log'][0][0][1],
                     'nkyotaku': json_['log'][0][0][2],
                     'dora_omote': json_['log'][0][2],
                     'dora_ura': json_['log'][0][3],
                     'result': json_['log'][0][-1][0],
                     'hora': '',
                     'hoju': '',
                     'nazo': '',  # kore ha nani?
                     'fu': '',
                     'han': '',
                     'yaku': ''
                     }
    if log_['kyoku']['result'] == '和了':
        log_['kyoku']['hora'] = json_["name"][json_["log"][0][-1][2][0]]
        log_['kyoku']['hoju'] = json_["name"][json_["log"][0][-1][2][1]] if json_["log"][0][-1][2][0] != json_["log"][0][-1][2][1] else ''
        log_['kyoku']['nazo'] = json_["log"][0][-1][2][2]

    print(log_['kyoku'])
    # exit()
    # fileio.write(data=json_, path=f"paifu/json/{'-'.join(map(str, json_['log'][0][0][:2]))}.json")


def main():
    [url2json(url=s) for s in fileio.read(path="paifu/txt/2019093001.txt")]

    for path in glob.glob('paifu/json/*-*.json'):
        pass
        # print(fileio.read(path=path)["log"][0][-1])


if __name__ == '__main__':
    main()