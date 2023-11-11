dictionary = {}
global name,money
name_list = []
money = ""
name = ""
print("------------------------------")
print("{:^23s}".format("員工薪資輸入"))
print("{:^20s}".format("若姓名處未輸入則代表結束"))
print("------------------------------")
while(True):
    name = input("請輸入姓名 : ")
    name_list.append(name)
    if name == "" :
        break
    else:
        money = input("請輸入薪資 : ")
        dictionary[name] = int(money)
        print()
print("------------------------------")
for name in dictionary:
    print(f'員工 {name} 的薪資為 {format(dictionary[name],",")}')
print("------------------------------")
money = 0
for i in range(len(dictionary)):
    money += dictionary[name_list[i]]
print(f'合計薪資 : {money:>10}')
print(f'平均薪資 : {format(round(money/len(dictionary),2),","):>10}')
