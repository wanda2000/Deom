import random
i=int(input("石头剪刀布游戏开始，玩家与机器之间的pk。0代表石头，1代表布，2代表剪刀\n"))
j=random.randrange(0,3)
while i!=0 and i!=1 and i!=2:
    i = int(input('重新输入i（0、1、2）\n'))
    if i==0 or i==1 or i==2:
        break
print("本函数以一方胜出结束")

while True:
    if i==0 and j==2 or i==1 and j==0 or i==2 and j==1:
        print("You are a winer\n并且你输入的是{0},机器输入的是{1}".format(i,j))
        break
    if i==0 and j==1 or i==1 and j==2 or i==2 and j==0:
        print("You are a loser并且你输入的是{0},机器输入的是{1}".format(i,j))
        i = int(input("游戏继续。0代表石头，1代表布，2代表剪刀\n"))
        j = random.randrange(0, 3)
        continue
    else:
        print("平局，并且你输入的是{0},机器输入的是{1}".format(i,j))
        flag = 0
        i = int(input("游戏继续。0代表石头，1代表布，2代表剪刀\n"))
        j = random.randrange(0, 3)
        continue