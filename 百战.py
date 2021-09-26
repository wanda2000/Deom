# import turtle
# x=turtle.Screen()
# t=turtle.pen()
# turtle.width(10)
# turtle.goto(100,100)
# turtle.goto(200,0)
# turtle.goto(140,-108)
# turtle.goto(0,-250)
# turtle.goto(-140,-108)
# turtle.goto(-200,0)
# turtle.goto(-100,100)
# turtle.goto(0,0)
#
# # while i >= 0:
# #     while j >= -100:
# #         i -= 0.015
# #         j -= 0.01
# #         turtle.goto(i,j)
#
# x.exitonclick()

# #replace 返回一个新对象，并没有改变字符串
# a='abcdef\
# ghijkmn\
# opqrst\
# uvwxyz'
# print(id(a))
# print(type(a))
# print(a)
# a=a.replace('a','熊')
# print(id(a))
# print(type(a))
# print(a)

#变量未被声明
# b='i am a good boy'
# print(b)
# del b
# print(b)

#int 格式不能转字符型的浮点数
# print(int(0x123))
# i = 0o123
# j = 0b01010010
# print(int(i),int(j))
# b=int(9.9)
# print(b)
# c = int(False)
# print(c)
# d = int ("456.78")
# print(d)

# a = 1000
# b = 1000
# print(a is b,id(a),id(b))
# print(a == b)
# y=5
# while 3<y<9:
#     print("1")
#     y+=1

# a = ~0b10101010
# print(bin(a))
'''
a=[1,3,5,7,7,7,5,3]
# for i in range(len(a)-1,-1,-1):
#     if a[i] == 7:
#         a.remove(7)
# print(a)

# for i in a[:]:
#      if i == 7:
#         a.remove(7)
# print(a)

# for i in a:
#     if i == 7:
#         a.remove(7)
# # print(a)
'''
# list_1=[]
# for i in a:
#     if i not in list_1:
#         list_1.append(i)
# print(list_1)
# a='abcdefghijklmnopqrstuvwxyz'
# a= a.replace('a','熊')
# print(a)

# for i in range(len(a)-1,-1,-1):
#     if a[i] == 7:
#         a.pop(i)
#         print(i)
# print(a)
# print(len(a))
# print(len(a))

# a = 'abcdefghijklmnopqrstuvwxyz'
# a = a.replace('a',"xiong")
# print(a)
#
# a = 'to be or not to be , this is a question!'
# b = a.split('be')
# print(a)
# print(b)

# import time
# time_01 = time.time()
# a=''
# for i in range(100000):
#     x='xiong'
#     a+=x
# time_02 = time.time()
# print(time_02-time_01)
#
# time_03 = time.time()
# c=[]
# for j in range(100000):
#     c.append('xiong')
# d=''.join(c)
# time_04 = time.time()
# print(time_04-time_03)

#棋盘
# import turtle
#
# t = turtle.Pen()
# color_01=("orange","gold","pink","brown","grey","purple","blue"\
#         ,"yellow","green","black","white","red","gold","pink","brown","grey","purple","blue","blue")
# x = [-200,100]
# y = [-20,-80]
# t.speed(10)
# for i in range(0,19):
#     t.penup()
#     t.color(color_01[i])
#     t.goto(x[0],100-10*i)
#     t.pendown()
#     t.goto(y[0],100-10*i)
#
# for j in range(0,19):
#     t.penup()
#     t.color(color_01[j])
#     t.goto(x[0]+10*j,x[1])
#     t.pendown()
#     t.goto(x[0]+10*j,y[1])
#
# t.hideturtle()
# turtle.done()

# r_1 = {"name":"xiong","age":18,"job":"student"}
# r_2 = {"name":"jun","age":18,"job":"techer"}
# r_3 = {"name":"yong","age":18,"job":"runer"}
# a = [r_1,r_2,r_3]
# for i in range(len(a)):
#         print(a[i].get("name"),a[i].get("age"),a[i].get("job"))


# a = [1,3,5,7,7,7,5,3,1]
# for j in a[:]:
#     if j == 7:
#         a.remove(j)
#     print(a)
#
# print("*****************************************")
# b = [1,3,5,7,7,7,5,3,1]
# for i in b:
#     if i == 7:
#         b.remove(i)
#     print(b)
#
# a = "*  to be or not to be , this is a 熊 question?  *"
# b = a.split(" ")
# print(b,type(b))
# print(a.startswith("to be or"),a.endswith("a question?"),len(a))
# print(a.find("o"),a.rfind("o"),a.isalnum())
# print(a.strip(),a.rstrip("*"),a.lstrip("*"))

# d = ["to be or not to be "]
# c = "*".join(d)
# print(c,type(c))

# a = "i love You"
# print(a.title(),a.upper(),a.lower(),a.capitalize(),a.swapcase())

#cneter() ljust() rjust()
a = "abcd"
print(a.center(10,"*"),a.rjust(10,"*"),a.ljust(10,"*"))