import random
i=int(input("石头剪刀布游戏开始，玩家与机器人小Q之间的pk。0代表石头，1代表布，2代表剪刀\n"))
print("==================================================================")
j=random.randrange(0,3)
print("游戏以你胜出结束\n")
while True:
    if i != 0 and i != 1 and i != 2:
        i = int(input('输入的信息有误，请重新输入0、1、2\
        (0代表石头，1代表布，2代表剪刀)\n'))
        continue
    if i==0 and j==2 or i==1 and j==0 or i==2 and j==1:
        print("You are a winer,并且你输入的是{0},机器小Q输入的是{1}".format(i,j))
        break
    if i==0 and j==1 or i==1 and j==2 or i==2 and j==0:
        print("小Q is a winer并且你输入的是{0},机器人小Q输入的是{1}".format(i,j))
        i = int(input("游戏继续。0代表石头，1代表布，2代表剪刀\n"))
        j = random.randrange(0, 3)
        continue
    else:
        print("平局，并且你输入的是{0},机器人小Q输入的是{1}".format(i,j))
        flag = 0
        i = int(input("游戏继续。0代表石头，1代表布，2代表剪刀\n"))
        j = random.randrange(0, 3)
        continue
print("==================================================================")