import glob
import json
import pathlib
import re
import urllib


def indent_paifu_txt(txtpath:pathlib.Path):
    ''' input_paifu_txt

    牌譜URLをJSON形式で保存

    Args:
        path (str): Paifu text path

    Returns:
        None

    Notes:
        - txtpath.nameは、yyyymmdd_99.txt となることを想定
            - yyyy: 試合日付（年）
            - mm: 試合日付（月）
            - dd: 試合日付（日）
            - 99: その日の何試合目か
    '''

    # Get date and number of match
    pat: str = r'(\d{8})_(\d{2}).txt'
    mat: str = re.match(pat, txtpath.name)

    date: str = mat.group(1)
    nmatch: str = mat.group(2)

    # Make output directory of json
    path_output_dir: str = pathlib.Path(f"./paifu/json/{date}_{nmatch}")
    if not path_output_dir.exists():
        path_output_dir.mkdir()

    # Read lines for text file
    lines: List[str] = []
    with txtpath.open(mode='r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    # Write json file
    for l in lines:
        # Convert URL to json
        url: str = urllib.parse.unquote(l)
        pat: str = r'https://tenhou.net/.*json=(.*)'
        mat: str = re.match(pat, url)

        json_ = json.loads(mat.group(1))

        # Write json file
        nkyoku: str = json_['log'][0][0][0]
        nhonba: str = json_['log'][0][0][1]

        path_output: pathlib.Path = pathlib.Path(f"{path_output_dir}/{date}_{nmatch}_{nkyoku}_{nhonba}.json")
        json.dump(json_, open(path_output, 'w') , ensure_ascii=False)

def main():
    # Make json file from text file
    path_input: pathlib.Parh = pathlib.Path('./paifu/txt')
    for txt in path_input.glob('*.txt'):
        indent_paifu_txt(txt)

if __name__ == '__main__':
    main()