## :bookmark_tabs: 数独問題をカメラで読み込み解いて3Dプリンターで解を書くのお勉強

参考リンク[^1]に触発され、機能ごとにお勉強したことをまとめました。

- 数独の解法は公開されているコードを集めて、各種アルゴリズムの比較をしてみたい
- 各機能がちゃんと動くことを確認する

以下3つの機能に分解して、それぞれ確認します。
### 画像から数字を読み取る

tesseractというpython libraryを使って画像から問題を読み取れることを確認します。
事前準備が必要です。

tesseract,opencv,PIL等のインストール
```bash
pip3 install pytesseract
apt-get install tesseract-ocr tesseract-ocr-jpn
```

読み込んだ画像を2値化することが前処理として重要なようです。
こちら[^2]を参考にして、以下の3つの方法を試してみました。
- 単純な閾値処理
- 適応的閾値処理(仕組みはこちら[^3]が詳しい)
- 大津の閾値処理
### 数独問題を解く

公開されているpythonソースを収集して動作することを確認。
アルゴリズムの違いと処理時間の比較ができればよい。

### 回答を3Dプリンターで書く

Gcodeのテンプレートを作成し、プリンターに合わせて設定等を調整。

## 参考リンク

[^1]:[GitHub Sudoku-Solving-3D-Printer](https://github.com/bytesizedengineering/Sudoku-Solving-3D-Printer)

[^2]:[OpenCV 画像のしきい値処理](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding)

[^3]:[OpenCV adaptiveThresholdの処理アルゴリズム](https://imagingsolution.net/program/python/opencv-python/adaptivethreshold_algorithm/)