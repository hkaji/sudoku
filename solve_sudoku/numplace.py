#
#  data.csvに問題データ
#  https://news.mynavi.jp/article/zeropython-54/
import csv, copy, pprint
# 問題データをCSVで指定 --- (*1)
QFILE = "data.csv"

# 問題データを読む --- (*2)
data = []
with open(QFILE, "rt") as f:
    for row in csv.reader(f):
        r = []
        for v in row:
            try:
                r.append(int(v.strip()))
            except:
                r.append(0)
        data += [r]
print("--- 問題データ ---")
pprint.pprint(data)

# 空白の部分を再帰的に解く --- (*3)
def set_num(vdata, idx):
    # 終了判定 --- (*4)
    if idx >= 81:
        pprint.pprint(vdata)
        return True
    # 空白があるか調べる --- (*5)
    col = idx % 9
    row = idx // 9
    if vdata[row][col] != 0:
        return set_num(vdata, idx + 1)
    # どの数字が利用可能か調べる --- (*6)
    u = {}
    for i in range(9):
        u[vdata[i][col]] = True
        u[vdata[row][i]] = True
    # 利用可能な数値を順に入れて再帰 --- (*7)
    for n in range(1, 10):
        if n in u: continue
        if not check3x3(vdata, col, row, n): continue
        ndata = copy.deepcopy(vdata) # リストをコピー
        ndata[row][col] = n
        if set_num(ndata, idx + 1): return True
    return False

# 3x3のマスの中も数字が重複しないか確認
def check3x3(vdata, col, row, val):
    c3 = col // 3 * 3
    r3 = row // 3 * 3
    u = {}
    for x in range(0, 3):
        for y in range(0, 3):
            n = vdata[r3 + y][c3 + x]
            u[n] = True
    return not val in u

# 結果表示
print("--- 完成データ ---")
set_num(data, 0)
print("ok")
