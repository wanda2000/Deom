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
# 数据类型*******
# import math
# a=3.0
# b=4.0
# c=5.0
# h=(a+b+c)/2
# s=math.sqrt(h*(h-a)*(h-b)*(h-c))
# print("{0:.2f}".format(s))

# import math
# r=float(input("输入圆的半径："))
# s=math.pi*r**2
# print("圆的面积为:{:.2f}".format(s))
# print("圆的面积为%f"%s)
# print(str.format("圆的面积为:{:.2f}",s))
# print("如果语句太长用,\
# you are a good boy")

# def do_bothing():
#     print("to be or not to be,this is a question!")
# a=do_bothing()
# print(type(a))

# import math
# def getValue(b,r,n):
#     v=b*math.pow(1+r,n)
#     return v
# a=getValue(5000,0.05,10)
# print("收益为：{:.2f}".format(a))
# print(str.format("收益为：{:.2f}",a))
# print("收益为：%f"%a)

# a=-12
# b=abs(a)
# print(a,b)

# b=int(input("输入本金b："))
# # r=int(input("输入利率r: "))
# # n=int(input("输入年数n："))
# # v=b*(1+r)**n
# # print(v)

# import datetime
# a=input("输入你的姓名：")
# b=int(input("输入你的出生年份："))
# c=datetime.date.today().year-b
# print("您好{0}，您的岁数是{1}".format(a,c))

#

# print("初始状态",a,b)
# print("初始状态{0:.2f},{1:.2f}".format(a,b))
# if a<b:
#     a,b=b,a
# print("结束状态",a,b)
# print("结束状态{0:.2f},{1:.2f}".format(a,b))

# import math
# x=float(input("输入数字x:"))
# if x>=0 :
#     y=math.sin(x)+2*math.sqrt(x+math.exp(4))-math.pow(x+1,3)
# else:
#     y=math.log(-5*x,math.e)-abs(math.pow(x,2)-8*x)/(7*x)+math.e
# print(y)

# i=1
# while i<=41:
#     mark=int(input("输入你的成绩："))
#     if mark>=90:
#         print("优")
#     elif mark>=80:
#         print("良")
#     elif mark>=70:
#         print("中")
#     elif mark>=60:
#         print("及格")
#     else:
#         print("不及格")
#     i+=1

# x=float(input("输入数字x:"))
# y=float(input("输入数字y:"))
# if x==0:
#     print("在y轴上")
# elif y==0:
#     print("在x轴上")
# elif x>0 and y>0:
#     print("在第一象限")
# elif x<0 and y>0:
#     print("在第二象限")
# elif x<0 and y<0:
#     print("在第三象限")
# else:
#     print("在第四象限")

# a=int(input("输入数字a："))
# b=int(input("输入数字b: "))
# c=int(input("输入数字c: "))
# print(a,b,c)
# if a<b:
#     a,b=b,a
# if a<c:
#     a,c=c,a
# if b<c:
#     b,c=c,b
# print(a,b,c)

# sun=0 ; sum_odd=0 ; sum_even=0 ; i=1
# while i<=100:
#     sun+=i
#     if i%2==0:
#         sum_even+=i
#     if i%2!=0:
#         sum_odd+=i
#     i+=1
# print(sun,sum_odd,sum_even)

# import math
# e=1 ;t=1; i=1
# while 1/t>=math.pow(10,-6):
#     t*=i
#     e+=1/t
#     i+=1
# print(e)

'''九九乘法表'''
# for i in range(1,10):
#     for j in range(1,10):
#         print("{0:1}*{1:1}={2:<3}".format(i,j,i*j),end='')
#     print('')
'''上三角、下三角'''
# for i in range(1,10):
#     j=1
#     while j<=i:
#         print("{0:1}*{1:1}={2:<3}".format(i, j, i * j), end='')
#         j+=1
#     print('')
# x=k=1
# while x<=9:
#     k=2*x-1
#     while k>x:
#         print(end="       ")
#         k-=1
#     for y in range(x,10):
#         print("{0:1}*{1:1}={2:<3}".format(x,y,x*y),end='')
#     print('')
#     x+=1
'''左上三角、右下三角'''
# x=k=1
# while x<=9:
#     for y in range(x,10):
#         print("{0:1}*{1:1}={2:<3}".format(x,y,x*y),end='')
#     print('')
#     x+=1
# i=1
# while i<=9:
#     k = 9
#     while k>i:
#         print(end="       ")
#         k-=1
#     for j in range(1,i+1):
#         print("{0:1}*{1:1}={2:<3}".format(i, j, i * j), end='')
#     print('')
#     i+=1
'''素数'''
# import math
# m=int(input("输入一个大于1的整数："))
# k=int(math.sqrt(m))
# for i in range(2,k+2):
#     if m%i==0:
#         break
# if i==k+1:
#     print(m,"是素数")
# else:
#     print("是和数")

import math
m=int(input("输入一个大于1的整数："))
k=int(math.sqrt(m))
flag=True
i=2
while i<k and flag:
    if 