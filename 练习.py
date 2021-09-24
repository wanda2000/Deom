#迷幻
# import turtle
# windows=turtle.Screen()
# t=turtle.Pen()
# for i in range(360):
#     t.forward(i)
#     t.left(59)
#
# windows.exitonclick()
#奥运五环
# import turtle
# window = turtle.Screen()
# turtle.showturtle()
# turtle.width(5)
# turtle.bgcolor("orange")
#
# turtle.color("red")
# turtle.penup()
# turtle.goto(-100,0)
# turtle.pendown()
# turtle.circle(50)
#
# turtle.color("blue")
# turtle.penup()
# turtle.goto(10,0)
# turtle.pendown()
# turtle.circle(50)
#
# turtle.color("yellow")
# turtle.penup()
# turtle.goto(120,0)
# turtle.pendown()
# turtle.circle(50)
#
# turtle.color("black")
# turtle.penup()
# turtle.goto(-50,-50)
# turtle.pendown()
# turtle.circle(50)
#
# turtle.color("green")
# turtle.penup()
# turtle.goto(60,-50)
# turtle.pendown()
# turtle.circle(50)
#
# turtle.color("white")
# turtle.penup()
# turtle.goto(0,100)
# turtle.pendown()
# turtle.write("奥运五环")
#
# window.exitonclick()

# import turtle
# windows=turtle.Screen()
# turtle.showturtle()
# turtle.width(6)
# #第一个矩形
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(90)
# #第二个矩形
# turtle.color("yellow")
# turtle.penup()
# turtle.goto(-150,0)
# turtle.pendown()
# turtle.left(180)
# turtle.forward(90)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(90)
# turtle.right(90)
# turtle.forward(100)
# #第三个矩形
# turtle.color("orange")
# turtle.penup()
# turtle.goto(0,-60)
# turtle.pendown()
# turtle.left(180)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(90)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(90)
# #第四个矩形
# turtle.color("red")
# turtle.penup()
# turtle.goto(-150,-60)
# turtle.pendown()
# turtle.left(180)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(100)
#
# windows.exitonclick()
#练习
# a = [10,20,\
#      30,40
#     ,50]
# print(a)
#
# a = -100
# b = -100
# print(id(a),type(a))
# print(id(b),type(b))
# del a,b
# a=divmod(13,3)
# print(a,type(a))
# b =int(a)
# print(b)
# b = 314E-2
# c = 4.999
# print(round(b),round(c))
# help()

#join和+号的运行时间的区别
# import time
# c = time.time()
# a=''
# for i in range(1000000):
#     x="xiong"
#     a+=x
# d = time.time()
# print("运行的时间是："+str(d-c))
#
# e = time.time()
# b=[]
# for i in range(1000000):
#     b.append("xiong")
# a=''.join(b)
# f = time.time()
# print("运行的时间是："+str(f-e))

#ord 和 chr
# a = "熊"
# b = 65
# print(ord(a),chr(b))

# 双套单，单套双
# a="I'm a good boy"
# print(a)

#''''''之中可以创建多行字符串
# a = '''myname = "熊俊勇"
# my_age = 19
# lover = "python"
# '''
# print(a)

# a={1:"as",2:"sf"}
# print(a[1])
#
# ls=[[1,2,3],[[4,5],6],[7,8]]
# print(len(ls))

# a=[
#     ['熊俊勇',18,'江西宜春'],
#     ['杨城',18,'江西赣州'],
#     ['肖鹏钒',18,'江西吉安'],
#     ['曹达超',18,'江西九江'],
#   ]
# print(len(a))
# for i in range(4):
#     for j in range(3):
#         print(a[i][j],end='\t')
#     print()

# a='ancdefghijklmnopqrstuvwxyz'
# a = a.replace('n','熊')
# print(a)
# print(type(a))
# print(a[::-1])
# print(a[1:])
# print(a[-8:-3:2])
# print(a[19:9:-1])
#
# #practice:
# 1、将
a=[1,3,5,7,7,7,5,3,2]
print(len(a))
for i in range(len(a)):
    for j in a:
        if j == 7:
            a.remove(j)
print(a)
