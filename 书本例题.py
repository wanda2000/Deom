#本文件不将保存什么东西
#print(round(18.67,-1),round(123.84,-2))
'''num=int(input("输入一个整数："))
while(num!=0):
    print(num%10,end='')
    num=num//10
#计算落体100米的距离
i=100
meter=100
h=0
j=0
while(j<=(2**10)):
    j=2**j
    meter+=i/j
    j+=1
print("%f,%f",(meter,i/(2**10)))
#吃桃数字
a=1
b=[1]
i=7
while i>0 :
    j=2*(a+1)
    b.append(j)
    i-=1
    a=j
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
print(b[6])
print(b[7])
#sn=1+11+111+1111+……………
import random
n=random.randint(1,11)
t1=1
i=1
sn=1
b=[1]
while i<=n :
    for j in range(i-1,i):
        t=b[j]*10+1
        b.append(t)
        sn+=t
        i+=1
print("n={0},sn={1}".format(n,sn))
'''
