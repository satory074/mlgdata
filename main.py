import urllib.parse
import myutil


def main():
    [print(urllib.parse.unquote(s)) for s in myutil.FileIO().load(path="paifu/2019093001.txt")]


if __name__ == '__main__':
    main()