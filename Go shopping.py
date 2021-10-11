j = int(input("输入您的工资："))
i = int(input("输入数字6开启购物模式:"))
x = (["-iphone",6888],["-MacPro",14800],["-小米6",2499],["-Coffee", 31],["-Book",60],["-Nike",699])
b = []
sum_01 = j
flag = 1
while i==6:
    print("本商店提供的商品有（您可以选择物品编号来购买）：")
    for y in range(len(x)):
        print(y,x[y][0],"\t",x[y][1])
    c = int(input("输入您要买的商品编号（输入666退出购物模式）:"))
    if c == 666:
        break
    # while flag:
    if c >len(x):
        c = int(input("输入的编号错误，请重新输入编号:\n"))
    for a in range(len(x)):
        if a==c:
            if sum_01<x[a][1]:
                print("您的工资不支持您买这件商品,请选择别的商品:",x[a])
                # c = int(input("请重新输入您要买的商品编号:"))
            else:
                j -= j-x[a][1]
                sum_01 -= j
                print("您的资金剩余：",sum)
                b.append(x[a])
                print("你的购物车中有：",b)
    flag = int(input("输入0结束购物模式，否则按任意数字购物继续"))
    if flag == 0:
        break
print("购物愉快，您剩余的资金为：{0},您的购物车中有；{1}".format(j,b[:]))