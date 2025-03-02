# python-umamusume
ウマ娘自動リセマラ周回を Python の [android-auto-play-opencv](https://github.com/noitaro/android-auto-play-opencv "android-auto-play-opencv") を使って実現させました。

## How to use
[NoxPlayer](https://jp.bignox.com/ "NoxPlayer") が必要です。

このリポジトリをダウンロードして、ライブラリをインストールして下さい。
```
pip install android-auto-play-opencv
```

### 実行
NoxPlayer の画面解像度を 960×540 に設定する。

事前にチュートリアルを1回終わらせて、スキップ出来る状態にする。
```
Python umamusume.py
```

### 修正履歴
+ 2023/12/16 データ連携ボタンの位置を修正
+ 2023/12/16 商品追加ダイアログを閉じるように修正
+ 2022/10/24 おさんぽチュートリアルに対応
+ 2022/01/01 2021年末～2022年始のイベント対応 : [@DenimPauel氏](https://github.com/DenimPauel)
+ 2021/12/8 楽曲取得に対応 : [@DenimPauel氏](https://github.com/DenimPauel)
+ 2021/11/21 日付をまたいだリセマラに対応 : [@DenimPauel氏](https://github.com/DenimPauel)
+ 2021/08/28 ハーフアニバーサリーに対応 : [@DenimPauel氏](https://github.com/DenimPauel)
+ 2021/06/20 複数端末に対応


### 複数端末リセマラ手順
https://noitaro.github.io/multi-startup/

![](multi-startup.gif)
```Python
# ↓複数デバイスを同時に操作したい場合、コメントを外す。
import inquirer  # pip install inquirer

# ↓複数デバイスを同時に操作したい場合、コメントを外す。
devicesselect = [
    inquirer.List(
        "device",
        message="デバイスを選択して下さい。",
        choices=aapo.adbl.devices
    )
]
selected = inquirer.prompt(devicesselect)
aapo.adbl.setdevice(selected['device'])
```

### 仮想環境
```Bash
python -m venv env1
pip install -r requirements.txt
```
