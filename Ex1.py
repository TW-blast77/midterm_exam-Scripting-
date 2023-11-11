from pkg import triangle_zhonxin

print("請輸入三角形的3個頂點座標")
print("----------------------------------")
for i in range(0,3):
    if i == 0:
        a = input("請輸入頂點 a 的坐標 : ").split(',')
        A = tuple(a)
    if i == 1:
        b = input("請輸入頂點 b 的坐標 : ").split(',')
        B = tuple(b)
    if i == 2:
        c = input("請輸入頂點 c 的坐標 : ").split(',')
        C = tuple(c)
print("----------------------------------")
XY = (triangle_zhonxin(A,B,C))
print(f'此三角形的重心為 : {XY[0],XY[1]}')