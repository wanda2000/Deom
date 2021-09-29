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
# a = "abcd"
# print(a.center(10,"*"),a.rjust(10,"*"),a.ljust(10,"*"))

# a = "xiong"
# print("{:0>8}".format(a))
# print("{:1^9}".format(a))
# print("{:4<9}".format(a))

# import io
# a = "i'm a good boy!!！"
# sio = io.StringIO(a)
# sio.getvalue()
# sio.seek(7)
# sio.write("g")
# print(sio.getvalue())
#
# a = [1,3,5,7,7,7,5,3,1]
# a.append('xiong')
# a.extend([1,2,3,4])
# a.insert(3,"you")
# a.remove(1)
# a.clear()
# print(a)
# a = (i*3 for i in range(10) if i%2 == 0)
# print(a.__next__())
# print(a.__next__())
# b = tuple(a)
# print(b)
#
# a = {
#     "A":["b","c"]
# }
# print(a)
#
# b = dict(A=["a","b"])
# c = dict([("name","xiong"),("age",18)])
# print(a)
# print(b)
# print(c)
# #
# # a = ["name","age"]
# # b = ["xiong",18]
# # c = dict(zip(a,b))
# # print(bin(hash("name")))
#
# a = {1,2,3,4}
# a.add(5)
# print(a)
# c = [1,43,2]
# b = set(c)
#
# print(a|b)
# print(a&b)
# print(a-b)
#
# a = list(range(10))
# print(a)
# a = int(input("输入一个数字"))
# if a>10:
#     print(a)
# else:
#     print("a 不大于10")

# a = {"name":"xong","age":18,"job":"student"}
# for i in a.keys():
#     print(i)
# for j in a.items():
#     print(j)
# for x in a.values():
#     print(x)

# for i in range(5):
#     for j in range(1,6):
#         print(i,end='\t')
#     print()
# count = 0
# salary = []
# while True:
#     a =input("输入员工的薪资：")
#     if a.upper() == 'Q':
#         print("录入完成")
#         break
#     if float(a) < 0:
#         print("输入的薪资有问题，请输入员工的薪资")
#         continue
#     count+=1
#     salary.append(float(a))
# print("员工数量是{0},员工薪资明细{1},平均工资{2}".format(count,salary,sum(salary)/count))

# a = ["xiong","jun","yong"]
# b = [18,18,18]
# c = ["老师","学生","程序员"]
# for i,j,k in zip(a,b,c):
#     print("{0},{1},{2}".format(i,j,k))
# a = [(a,b) for a in range(10) for b in range(20)]
# print(a)
#
# a = "i'm a good boy and i like sports"
# d = {c:a.count(c) for c in a}
# print(d)
#
# import io
# a = "i'am a good boy"
# sio =io.StringIO(a)
# sio.getvalue()
# sio.seek(4)
# sio.write("熊")
# print(sio.getvalue())