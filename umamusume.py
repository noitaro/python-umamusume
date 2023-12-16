# This Python file uses the following encoding: utf-8
# 解像度 960x540 で作ってあるので、実行前にNoxの解像度を変更して下さい。

# pip install -U android-auto-play-opencv
from android_auto_play_opencv import AapoManager
import datetime
import traceback

# ↓複数デバイスを同時に操作したい場合、コメントを外す。
#import inquirer  # pip install inquirer

import os

adbpathCandidates = [
    'C:\\Program Files\\Nox\\bin\\',
    'C:\\Program Files (x86)\\Nox64\\bin\\',
    'C:\\Program Files (x86)\\Nox\\bin\\',
    'D:\\Program Files\\Nox\\bin\\'
]

ROBY_STABLE = 5  # ロビー安定を判断する回数

aapo: AapoManager = None

# 実行フォルダ取得
file_path: str = os.path.dirname(__file__)
# 実行フォルダが取得できない場合、カレントフォルダを指定
if file_path == '':
    file_path = '.'

print('終わらせたい時はCtrl+C')
def main():

    global aapo
    adbpath: str = None
    for i in range(len(adbpathCandidates)):
        if(os.path.exists(adbpathCandidates[i]) == True):
            adbpath = adbpathCandidates[i]
            break

    if adbpath is None:
        print('adb.exe が見つからないため、終了します。')
        return

    aapo = AapoManager(adbpath)
    mode: int = 0  # モード0(リセット)
    folderName: str = ''
    stackCount: int = 0
    present_ok: bool = False

    robyCount: int = 0  # ロビーカウンタ(変数の初期化)

    GATYA_INIT_SETTING_IS_PRETTYDARBY = True
    
    # ↓複数デバイスを同時に操作したい場合、コメントを外す。
    #devicesselect = [
    #   inquirer.List(
    #       "device",
    #       message="デバイスを選択して下さい。",
    #       choices=aapo.adbl.devices
    #   )
    #]
    #selected = inquirer.prompt(devicesselect)
    #aapo.adbl.setdevice(selected['device'])

    # スタート
    start()

    print('■■■ リセマラ 開始 ■■■')

    while True:
        # 画面キャプチャ
        aapo.screencap()

        # 早送りボタンは常にタップ
        if aapo.touchImg(file_path +'/umamusume/hayaokuri.png'):
            # タップ出来たら待機
            aapo.sleep(1)

        # 通信エラー時は、タイトルへを押す)
        elif aapo.chkImg(file_path +'/umamusume/communicationerror.png'):
            aapo.touchImg(file_path +'/umamusume/tothetitle.png')
            aapo.sleep(1)

        # Google Playダイアログが出たら、キャンセルボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/google-play.png'):
            aapo.touchImg(file_path +'/umamusume/cancel.png')
            aapo.sleep(1)

        # アカウント連携ダイアログが出たら、後でするボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/account.png'):
            print('■■■ アカウント連携設定のお願い -> 後で ■■■')
            aapo.touchImg(file_path +'/umamusume/atode.png')
            aapo.sleep(1)

        # チュートリアルダイアログが出たら、スキップボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/tutorial.png'):
            print('■■■ チュートリアル確認 -> スキップ ■■■')
            aapo.touchImg(file_path +'/umamusume/skip.png')
            aapo.sleep(1)

        # トレーナー登録ダイアログが出たら、
        elif aapo.chkImg(file_path +'/umamusume/trainer.png'):
            print('■■■ トレーナー登録 開始 ■■■')
            # トレーナー名入力の位置をタップ
            aapo.touchPos(405, 430)
            aapo.sleep(1)
            # abc と入力
            aapo.inputtext('abc')
            aapo.sleep(1)
            # トレーナー名入力の位置をタップ
            aapo.touchPos(270, 430)
            aapo.sleep(1)
            # 登録ボタンの位置をタップ1
            aapo.touchPos(270, 630)
            aapo.sleep(1)
            # 登録ボタンの位置をタップ2
            aapo.touchPos(270, 630)
            aapo.sleep(1)
            # OKボタンの位置をタップ
            aapo.touchPos(405, 630)
            aapo.sleep(1)
            print('■■■ トレーナー登録 終了 ■■■')

        # データダウンロードダイアログが出たら、OKボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/datadownload.png'):
            print('■■■ データダウンロード -> OK ■■■')
            aapo.touchImg(file_path +'/umamusume/ok.png')
            aapo.sleep(1)

        # お知らせダイアログが出たら、閉じるボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/osirase.png'):
            print('■■■ お知らせ -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # おさんぽチュートリアルが出たら、次へボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/osanpo.png'):
            print('■■■ おさんぽ 開始 ■■■')
            # 次へボタンの位置を3回タップ
            aapo.touchPos(270, 900)
            aapo.sleep(1)
            aapo.touchPos(270, 900)
            aapo.sleep(1)
            aapo.touchPos(270, 900)
            aapo.sleep(1)
            print('■■■ おさんぽ 終了 ■■■')

        # 外部リンク確認
        elif aapo.chkImg(file_path +'/umamusume/gaibulink.png'):
            print('■■■ 外部リンク確認 -> キャンセル ■■■')
            # キャンセルボタンをタップ
            aapo.touchImg(file_path +'/umamusume/cancel.png')
            aapo.sleep(1)

        # 交換確認
        elif aapo.chkImg(file_path +'/umamusume/koukankakunin.png'):
            print('■■■ 交換確認 -> 閉じる ■■■')
            # 閉じるボタンをタップ
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # 商品追加ダイアログが出たら、キャンセルボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/syohin-tuika.png'):
            print('■■■ 商品追加 -> キャンセル ■■■')
            aapo.touchImg(file_path +'/umamusume/cancel.png')
            aapo.sleep(1)

        # ピックアップ選択ダイアログが出たら、キャンセルボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/pickup-sentaku.png'):
            print('■■■ ピックアップ選択 -> キャンセル ■■■')
            aapo.touchImg(file_path +'/umamusume/cancel.png')
            aapo.sleep(1)

        # メインストーリー開放ダイアログが出たら、閉じるボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/main-story.png'):
            print('■■■ メインストーリー解放 -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # ウマ娘ストーリー開放ダイアログが出たら、閉じるボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/umamusume-story.png'):
            print('■■■ ウマ娘ストーリー解放 -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # ウマ娘詳細ダイアログが出たら、閉じるボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/umamusume-syosai.png'):
            print('■■■ ガチャ登場育成ウマ娘詳細 -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # 楽曲獲得ダイアログが出たら、閉じるボタンをタップ
        elif aapo.chkImg(file_path +'/umamusume/gakkyoku.png'):
            print('■■■ 楽曲取得 -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # 日付が変わりましたが表示されたら、
        elif aapo.chkImg(file_path +'/umamusume/newday.png'):
            print('■■■ 日付変更 -> OK ■■■')
            aapo.touchImg(file_path +'/umamusume/OK.png')
            aapo.sleep(1)

        # 受取完了ダイアログが出たら、閉じるの位置をタップ
        elif aapo.chkImg(file_path +'/umamusume/uketorikanryo.png'):
            print('■■■ 受取完了 -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # 衣装獲得ダイアログが出たら、閉じるの位置をタップ
        elif aapo.chkImg(file_path +'/umamusume/isyoget.png'):
            print('■■■ 衣装獲得 -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # ガチャストック通知が出たら、閉じるの位置をタップ
        elif aapo.chkImg(file_path +'/umamusume/gatyaStockNotification.png'):
            print('■■■ ガチャストック通知 -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)
            
        # プレゼントダイアログが出たら、一括受取の位置をタップ
        elif present_ok == False and aapo.chkImg(file_path +'/umamusume/present.png'):
            print('■■■ プレゼント -> 一括受取 ■■■')
            aapo.touchImg(file_path +'/umamusume/ikkatuuketori1.png')
            present_ok = True
            aapo.sleep(1)

        # プレゼントを受け取った後で一括受取が押せなくなったら、閉じるの位置をタップ
        elif present_ok == True and aapo.chkImg(file_path +'/umamusume/ikkatuuketori2.png'):
            print('■■■ プレゼント -> 閉じる ■■■')
            aapo.touchImg(file_path +'/umamusume/close.png')
            aapo.sleep(1)

        # ガチャボタンを見つけたら、ロビーと判断し、プレゼントを受け取っていない場合、
        elif present_ok == False and aapo.chkImg(file_path +'/umamusume/roby.png'):

            # お知らせが差し込まれる場合があるため、ロビーが安定するまで、robyStable回空ループさせる。
            robyCount += 1
            if robyCount < ROBY_STABLE:
                print(f'■ ロビー待機: {robyCount} -> プレゼント')
                aapo.sleep(1)  # 小休止を入れる
                continue
                
            robyCount = 0

            # プレゼントの位置をタップ
            aapo.touchPos(490, 680)
            aapo.sleep(1)

        # ガチャボタンを見つけたら、ロビーと判断し、プレゼントを受け取った後、
        elif present_ok == True and aapo.chkImg(file_path +'/umamusume/roby.png'):

            # 実績ログが終わるまで待機（メニューボタンが隠れて押せないから）
            robyCount += 1
            if robyCount < ROBY_STABLE:
                print(f'■ ロビー待機: {robyCount} -> データ連携')
                aapo.sleep(1)  # 小休止を入れる
                continue

            robyCount = 0

            # メニューボタンの位置をタップ
            aapo.touchPos(490, 50)
            aapo.sleep(2)

            print('■■■ データ連携 開始 ■■■')

            # データ連携の位置をタップ1
            aapo.screencap()
            aapo.sleep(1)
            aapo.touchImg(file_path +'/umamusume/data-renkei.png')
            aapo.sleep(1)
            # データ連携の位置をタップ2
            aapo.touchPos(405, 640)
            aapo.sleep(1)
            # 連携パスワードの位置をタップ
            aapo.touchPos(450, 550)
            aapo.sleep(1)
            # 設定の位置をタップ
            aapo.touchPos(405, 640)
            aapo.sleep(1)
            # 連携パスワード入力の位置をタップ
            aapo.touchPos(270, 405)
            aapo.sleep(1)
            # 1qazXSW2 と入力
            aapo.inputtext('1qazXSW2')
            aapo.sleep(1)
            # 確認入力の位置をタップ1
            aapo.touchPos(270, 505)
            aapo.sleep(1)
            # 確認入力の位置をタップ2
            aapo.touchPos(270, 505)
            aapo.sleep(1)
            # 1qazXSW2 と入力
            aapo.inputtext('1qazXSW2')
            aapo.sleep(1)
            # プライバシーポリシーの位置をタップ1
            aapo.touchPos(135, 620)
            aapo.sleep(1)
            # プライバシーポリシーの位置をタップ2
            aapo.touchPos(135, 620)
            aapo.sleep(1)
            # OKの位置をタップ
            aapo.touchPos(405, 680)
            aapo.sleep(1)
            # 画面キャプチャ
            aapo.screencap()

            # フォルダ名がカラの場合セット
            now_datatime_string = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            if len(folderName) == 0: folderName = now_datatime_string
            
            # スクショを保存
            aapo.imgSave(f'gatya/{folderName}/screenshot_{now_datatime_string}.png')
            
            print('■■■ データ連携 終了 ■■■')

            aapo.sleep(1)
            # 閉じるの位置をタップ
            aapo.touchPos(270, 630)
            aapo.sleep(3)
            # ガチャボタンの位置をタップ
            aapo.touchPos(480, 930)
            aapo.sleep(2)

        # 無料ガチャボタンがあれば引く。
        elif aapo.touchImg(file_path +'/umamusume/onegatyaforfree.png'):
            # タップ出来たら待機
            aapo.sleep(1)

        # ガチャを引く！
        elif aapo.touchImg(file_path +'/umamusume/gatyahiku.png'):
            print('■■■ ガチャを引く ■■■')
            # タップ出来たら待機
            aapo.sleep(1)

        # もう1回引くボタンをタップ
        elif aapo.touchImg(file_path +'/umamusume/pickagain.png'):
            print('■■■ もう一回引く ■■■')
            # タップ出来たら待機
            aapo.sleep(1)

        # 購入するボタンが出たら、ガチャ終了
        elif aapo.chkImg(file_path +'/umamusume/konyusuru.png'):
            print('■■■ リセマラ 終了 ■■■')

            # リセット
            reset()
            # スタート
            start()

            mode = 0  # モード0(リセット)
            folderName = ''
            stackCount = 0
            robyCount = 0
            present_ok = False

        # ガチャ結果
        elif aapo.chkImg(file_path +'/umamusume/gatya-kekka.png'):

            # フォルダ名がカラの場合セット
            now_datatime_string = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            if len(folderName) == 0: folderName = now_datatime_string

            # スクショを保存
            aapo.sleep(1)
            aapo.screencap()  # スクリーンリフレッシュ（写真が取れない場合がある。ボタン押下時のタイマーよりここのほうが確実な気がする。)
            aapo.imgSave(f'gatya/{folderName}/screenshot_{now_datatime_string}.png')
            aapo.sleep(2)

        # 左上にピンクガチャタイトルが出た時
        elif aapo.chkImg(file_path +'/umamusume/gatyaselected.png'):

            # 無償の10回引くボタンがあるか？
            if aapo.touchImg(file_path +'/umamusume/10-kaihiku.png'):
                aapo.sleep(1)
            else:
                # 無ければ、次のページへ
                aapo.touchPos(460, 580)
                aapo.sleep(1)

        # モードが0(リセット)の場合
        elif mode == 0:
            # ハンバーガーメニューボタンをタップ
            if aapo.touchImg(file_path +'/umamusume/hanba-ga-menu.png'):
                print('■■■ ユーザーデータ削除 開始 ■■■')

                # タップ出来たら待機
                aapo.sleep(1)
                # ユーザーデータ削除の位置をタップ1
                aapo.touchPos(270, 750)
                aapo.sleep(1)
                # ユーザーデータ削除の位置をタップ2
                aapo.touchPos(405, 630)
                aapo.sleep(1)
                # ユーザーデータ削除の位置をタップ3
                aapo.touchPos(405, 630)
                aapo.sleep(1)

                print('■■■ ユーザーデータ削除 終了 ■■■')

                # 閉じるの位置をタップ
                aapo.touchPos(270, 630)
                aapo.sleep(1)
                # モードを1(チュートリアル)に変更
                mode = 1

        # モードが1(チュートリアル)の場合
        elif mode == 1:
            # ロゴをタップ
            if aapo.touchImg(file_path +'/umamusume/logo.png'):
                # タップ出来たら待機
                aapo.sleep(1)

            # 同意をタップ
            elif aapo.touchImg(file_path +'/umamusume/doui.png'):
                # タップ出来たら待機
                aapo.sleep(1)

        # スタック対策 起動後STARTが表示されない、アンドロイド画面(アプリが落ちた場合)
        if aapo.chkImg(file_path +'/umamusume/stack.png') or \
        aapo.chkImg(file_path +'/umamusume/umamusumegameicon.png'):
            print(f'スタック: {stackCount}')
            aapo.sleep(1)
            stackCount = stackCount + 1
            if stackCount > 10:
                # リセット
                reset()
                # スタート
                start()

                mode = 0  # モード0(リセット)
                folderName = ''
                stackCount = 0
                robyCount = 0
                present_ok = False
        else:
            stackCount = 0


def start():
    # アプリ起動
    aapo.start(
        'jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity')
    aapo.sleep(10)
    return


def reset():
    print('■■■ キャッシュ削除 開始 ■■■')

    # ホームキーを押す
    aapo.inputkeyevent(3)
    aapo.sleep(1)
    # タスクキーを押す
    aapo.inputkeyevent(187)
    aapo.sleep(1)
    # すべて消去の位置をタップ
    aapo.touchPos(700, 55)
    aapo.sleep(1)

    # ウマ娘アイコンを探して、ロングタップ、キャッシュを消す
    aapo.screencap()
    found, x, y = aapo.chkImg2(file_path +'/umamusume/umamusumegameicon.png')
    if found:
        aapo.longTouchPos(x, y, 1000)
        aapo.sleep(1)

        # プロパティ表示
        aapo.screencap()
        aapo.touchImg(file_path +'/umamusume/appproperty.png')
        aapo.sleep(1)

        # ストレージ表示
        aapo.screencap()
        aapo.touchImg(file_path +'/umamusume/calculatingstorage.png')
        aapo.sleep(1)

        # キャッシュを削除
        aapo.screencap()
        aapo.touchImg(file_path +'/umamusume/clearcache.png')
        aapo.sleep(1)

        # タスクキーを押す
        aapo.inputkeyevent(187)
        aapo.sleep(1)
        # すべて消去の位置をタップ
        aapo.touchPos(700, 55)
        aapo.sleep(1)

    print('■■■ キャッシュ削除 終了 ■■■')

    return

# メイン関数を実行(Ctrl+Cで終了)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception:
        print(traceback.format_exc())
        input('エンターキーを押すと終了します。')