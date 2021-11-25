## \:note:数独問題をカメラで読み込み解いて3Dプリンターで解を書くのお勉強

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
### 数独問題を解く

公開されているpythonソースを収集して動作することを確認。
アルゴリズムの違いと処理時間の比較ができればよい。

### 回答を3Dプリンターで書く

Gcodeのテンプレートを作成し、プリンターに合わせて設定等を調整。

## 参考リンク

[^1]:[GitHub Sudoku-Solving-3D-Printer](https://github.com/bytesizedengineering/Sudoku-Solving-3D-Printer)