dictionary = {}
print(f"""------------------------------
{"員工薪資輸入":^23s}
{"若姓名處未輸入則代表結束":^20s}
------------------------------""")
while(True):
    name = input("請輸入姓名 : ")
    if name == "" : break
    else:
        dictionary[name] = int(input("請輸入薪資 : "))
        print()

print("------------------------------")
for k, v in dictionary.items(): print(f"員工 {k} 的薪資為 {v}")
print("------------------------------")

print(f'合計薪資:{sum(dictionary.values()):>14}')