from pkg import read_json ,print_json, process_data, write_json
MENU_FILE = 'menu.json' # 輸入檔案名稱
OUTPUT_FILE = 'output.json' # 輸出檔案名稱
new_json = {
    "name": "海鮮燉飯",
    "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
}

dictionary = read_json(MENU_FILE)
dictionary["categories"][1]["items"].append(new_json)
print(dictionary["categories"][1]["items"])
print_json(dictionary)
discount = float(input("請輸入折扣率(0.0 ~ 1.0):"))
process_data(dictionary,discount)
write_json(dictionary,OUTPUT_FILE)
