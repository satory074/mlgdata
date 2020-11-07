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

def reformat_json(json_: dict):
    """
    天鳳牌譜JSONをreformat

    @args: dict | 天鳳牌譜URLを変換した天鳳牌譜JSON
    @return: dict | reformatした天鳳牌譜JSON
    """

    # log
    di_kyoku = {
        'nkyoku': json_['log'][0][0][0],
        'nhonba': json_['log'][0][0][1],
        'nkyotaku': json_['log'][0][0][2],
        'dora_omote': json_['log'][0][2],
        'dora_ura': json_['log'][0][3],
        'result': json_['log'][0][-1][0],
        'hora': '',
        'hoju': '',
        'nazo': '',  # kore ha nani?
        'tensu': '',
        'yaku': []
        }

    if di_kyoku['result'] == '和了':
        di_kyoku['hora'] = json_["name"][json_["log"][0][-1][2][0]]
        di_kyoku['hoju'] = json_["name"][json_["log"][0][-1][2][1]] if json_["log"][0][-1][2][0] != json_["log"][0][-1][2][1] else ''
        di_kyoku['nazo'] = json_["log"][0][-1][2][2]
        di_kyoku['tensu'] = json_["log"][0][-1][2][3]
        di_kyoku['yaku'] = json_["log"][0][-1][2][4:]

    di_player = {
        json_['name'][i].split('（')[0]: {
            'team': json_['name'][i][-3:-1],
            'mochiten': json_['log'][0][1][i],
            'shushi':  json_['log'][0][-1][1][i],
            'haipai': json_['log'][0][3*i+4],
            'tsumopai': json_['log'][0][3*i+5],
            'sutepai': json_['log'][0][3*i+6]
        } for i in range(4)
    }

    json_['log'] = {
        'kyoku': di_kyoku,
        'player': di_player
        }

    return json_

def url2json(url: str):
    """
    天鳳牌譜URLをJSON形式で再保存

    @args: url | tenhou paifu url
    """
    json_ = json.loads(urllib.parse.unquote(url).split('json=')[1])
    fileio.write(data=json_, path=f"paifu/json/{json_['log'][0][0][0]}-{json_['log'][0][0][1]}.json")

    json_fmt = reformat_json(json_)
    fileio.write(data=json_, path=f"paifu/json-format/{json_['log']['kyoku']['nkyoku']}-{json_['log']['kyoku']['nhonba']}.json")


def main():
    [url2json(url=s) for s in fileio.read(path="paifu/txt/2019093001.txt")]

    # for path in glob.glob('paifu/json/*-*.json'):
    #     print(fileio.read(path=path))


if __name__ == '__main__':
    main()