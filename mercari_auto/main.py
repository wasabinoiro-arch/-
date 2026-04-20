import csv
import subprocess

file_path = "products.csv"
products = []

with open(file_path, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(row)

sold_id = input("売れた商品のidを入れてください: ").strip()

sold_product = None
for p in products:
    if p["id"] == sold_id:
        sold_product = p
        break

if not sold_product:
    print("商品見つからない")
    exit()

group_id = sold_product["group_id"]

next_product = None
for p in products:
    if p["group_id"] == group_id and p["status"] == "未出品":
        next_product = p
        break

if not next_product:
    print("出せる商品なし")
    exit()

def copy_to_clipboard(text: str) -> None:
    subprocess.run("pbcopy", text=True, input=text, check=True)

print("\n==============================")
print("次に出す商品")
print("==============================")
print("id:", next_product["id"])
print("title:", next_product["title"])
print("price:", next_product["price"])
print("description:", next_product["description"])
print("image_path:", next_product["image_path"])

# 1. タイトル
copy_to_clipboard(next_product["title"])
print("\n[1/3] タイトルをコピーしました")
print("メルカリの商品名欄で ⌘V してください")
input("貼れたら Enter: ")

# 2. 説明文
copy_to_clipboard(next_product["description"])
print("\n[2/3] 説明文をコピーしました")
print("メルカリの説明欄で ⌘V してください")
input("貼れたら Enter: ")

# 3. 価格
copy_to_clipboard(next_product["price"])
print("\n[3/3] 価格をコピーしました")
print("メルカリの価格欄で ⌘V してください")
input("貼れたら Enter: ")

print("\n連続コピー完了です")