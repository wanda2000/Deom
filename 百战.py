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
# c = 5
# def Max_01(a,b):
#     '''这是一个求最大值的函数'''
#     global c
#     if a>b:
#         print("较大值为a:",a)
#     else:
#         print("较大值为b：",b)
#     print(locals())
#     print(globals())
#     return([a,b,c])
# print(Max_01(10,20))
# import math
# import time
# def time_01():
#     '''测试局部变量和全局变量的时间'''
#     start = time.time()
#     for i in range(10000000):
#         math.sqrt(30)
#     end = time.time()
#     print("执行的时间是{0}：".format(end-start))
# def time_02():
#     start = time.time()
#     b = math.sqrt
#     for j in range(10000000):
#         b(30)
#     end = time.time()
#     print("执行的时间是{0}：".format(end-start))
# print(time_01())
# print(time_02())

# import copy
# a = (10,20,[30,40])
# b = copy.copy(a)
# print(id(a))
# def mpy_01(m):
#     print(id(m))
#     m[2][0] = 888
#     return(m)
# print(mpy_01(b))
# print(a)
# def mypy_01(a,b,**c):
#     print(a,b,c)
# mypy_01(1,2,name="xiong",age=18)
# g = [lambda a:a*2 , lambda b:b*2 , lambda c:c*2]
# print(g[0](6),g[1](7),g[2](10))
# a = 10
# b = 10
# dict = {"a":10,"b":20}
# print(eval("a+b",dict))
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return(n*factorial(n-1))
# for i in range(10):
#     print(i,"!=",factorial(i))
# def mypy_01():
#     print("running")
#     def mypy_02():
#         print("running")
#     mypy_02()
# print(mypy_01())
# def mypy_01(isChinese,name,familyname):
#     def mypy_02(a,b):
#             print("{0},{1}".format(a,b))
#     if isChinese:
#         mypy_02(familyname,name)
#     else:
#         mypy_02(name,familyname)
# print(mypy_01(True,"junyong","xiong"))
# def mypy_01(a):
#     b = str(a)
#     c = b[::-1]
#     return(c)
# print(mypy_01(3456))

# def max_01(a,b):
#     '''本函数是求两个数之间的最大值'''
#     if a>b:
#         print("较大数为：{0}".format(a))
#     else :
#         print("最大数为：{0}".format(0))
# max_01(10,9)
# help(max_01.__doc__)
#
# print("********************************")
#
# def print_start(a,b):
#     return((a+b)/2)
#
# c = print_start(10,20)
# print(c)
#
# a=10
# def global_01():
#         a = 100
#         print(a)
#         print(locals())
#         print(globals())
#
# global_01()
# print(a)
# class stident():
#     school = "jxkjsfdx"
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def score_01(self):
#         print(self.name,"分数是：",self.score)
#         print("你的公司是：",stident.school)
# b = stident("熊俊勇",100)
# b.score_01()
#
# print(dir(stident))
# print(stident.__dict__)
# print(isinstance(stident,type))

# class Student_01:
#     company = "iong"
#     @staticmethod
#     def add(a,b):
#         print("{0}+{1} = {2}".format(a,b,(a+b)))
#         return a+b
# Student_01.add(10,20)

# class Acountsalary:
#     def __call__(self,salary):
#         daysalary = salary//30
#         hourday = daysalary//8
#         return dict(daysalary=daysalary,hoursalary=hourday)
# s1 = Acountsalary()
# print(s1(20000))

# class Student:
#     '''类属性'''
#     company = "iong"
#     count = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.count = Student.count+1
#     def say_hi(self):
#         print("名字是{0},年龄是{1}".format(self.name,self.age))
#         print("输入了{0}条信息".format(Student.count))
# s1 = Student("熊俊勇",19)
# s2  = Student("gao",20)
# s3 = Student("1",30)
# s1.say_hi()

# class classmethod:
#     '''类方法'''
#     company = "iong"
#     @classmethod
#     def abc(cls):
#         print(cls.company)
# classmethod.abc()
#
# class Vo:
#     '''静态类方法'''
#     @staticmethod
#     def cde(a,b):
#         print("{0}+{1}={2}".format(a,b,(a+b)))
# Vo.cde(10,20)

# class Vo:
#     def __call__(self,):
#         print("销毁的对象{0}".format(self))
# p1 = Vo()
# p2 = Vo()
# del p2
# print("程序结束)
# class Book:
#     __company = "iong"
#
#     def __init__(self,name,age):
#         self.name = name
#         self.__age  = age
#     def __work(self):
#         print("好好工作，天天向上")
#         print("公司名字是{0}".format(Book.__company))
#         print("年龄是{0}".format(self.__age))
# e = Book("xiong",19)
# e._Book__work()
# print(dir(Book))
# print(Book.__dict__)
# import turtle
# class MyRectangle:
#     def __init__(self,x = 0,y = 0,width = 100,height = 100):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def GetArea(self):
#         print(self.width * self.height)
#     def GetPerimeter(self):
#         print(2*(self.width+self.height))
#     def Draw(self):
#         p = turtle.Pen()
#         turtle.width(10)
#         turtle.speed(8)
#         p.penup()
#         p.goto(self.x,self.y)
#         p.pendown()
#         p.goto(self.x,self.height)
#         p.goto(self.width,self.height)
#         p.goto(self.width,self.x)
#         p.goto(self.x,self.y)
#
#         turtle.done()
# tem_01 = MyRectangle(x = 9,y = 9,width = 200,height = 200)
# tem_01.GetArea()
# tem_01.GetPerimeter()
# tem_01.Draw()
# class Penson:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def M_01(self):
#         print("我的年龄是：",self.age)
#     def M_02(self):
#         print("我的名字是{0}".format(self.name))
#
# class Student(Penson):
#
#     def __init__(self,name,age,score):
#         Penson.__init__(self,name,age)
#         self.score = score
#     def M_02(self):
#         print("报告，我的名字是：{0}".format(self.name))
# class Tercher(Penson):
#     def __init__(self, name, age, score):
#         Penson.__init__(self, name, age)
#         self.score = score
# s = Student("xiong",18,90)
# s.M_01()
# s.M_02()
#
# c = Tercher("xiong",10,90)
# c.M_01()
# c.M_02()

# class M_01:
#     pass
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @property
#     def M_02(self):
#         print(self.age,self.name)
#         return self.age
#     @M_02.setter
#     def M_03(self,age):
#         if 0<age<100:
#             self.age = age
#         else:
#             print("输入的年龄有误")
# a = M_01("ion",190)
# print(a.age)
# a.M_03 = 1000
# class A :
#     def A_01(self):
#         print("a:",self)
#
# class B(A):
#     def A_01(self):
#         # A.A_01(self)
#         super().A_01()
#         print("B:",self)
#
# B().A_01()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def Student(self):
#         print("Hello World!!!")
#         print("我的名字是{},我的年龄是{}".format(self.name,self.age))
# a = Person("熊俊勇",19)
# a.Student()

# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)
#
# sum_01 = 0
# for i in range(10,0,-1):
#     sum_01+=i
# print(sum_01)


# import math
# a = [i for i in range(100) if i%2 != 0]
# print(type(a))
# total = sum(a)
# print(total)
#
# b = [i for i in range(101) if i%2 == 0]
# total = sum(b)
# print(total)



