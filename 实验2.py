#比较id值
'''
=2
y=2
print(x==y)
print(x is y)
'''
x=y=[1,2,3,4,5]
print(x==y)
print(x is y)
x.append(6)
z=[1,2,3,4,5,6]
print(z==x)
print(z==y)
print(z is x)
print(z is y)
