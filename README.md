# PySide6を使ったImage Viewer
ImgSimによる画像の類似度評価
## 環境
* Windows 11
* Python 3.12.7
* requirements.txtを参照

[OpenCVのライセンス](https://opencv.org/license/)

[PySideのライセンス](https://doc.qt.io/qtforpython-6/licenses.html)

[imgsimのライセンス](https://pypi.org/project/imgsim/#description)

## ソースファイル
| ファイル名 | 概要 |
|----------|------|
| imagesetdialog.py | 画像セットのクラスを実装 |
| imageview.py | 画像のビュークラスを実装 |
| mainwindow.py | メインウィンドウクラスを実装 |
| pyimgsim.py | メインプログラム<br>クラス間のSignsl, Slotの設定 |
｜mainwindow.ui | メインウィンドウのレイアウト<br>PySide6のパッケージフォルダ内の<br>designer.exeを使用 |
| ui_mainwindow.py | Scripts内のpyside6-uic.exeを<br>使用してmainwindow.uiから変換<br>mainwindow.py で使用 |
| imagesetdialog.ui | 画像セットの操作を行うダイアログボックス<br>PySide6のパッケージフォルダ内の<br>designer.exeを使用 |
 |ui_imagesetdialog.py | Scripts内のpyside6-uic.exeを<br>imagesetdialog.uiから変換<br>mainwindow.py で使用 |
