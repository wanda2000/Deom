import random
l=random.randint(0,99)
g=int(input("input a number"))
l_1=l//10
l_2=l%10
g_1=g//10
g_2=g%10
print("the number is :",l)
if (g==l):
    print("you win 10000")
elif g_2==l_1 and g_1==l_2:
    print("you win 3000")
elif g_1==l_2 \
    or g_2==l_2\
    or g_2==l_2 \
    or g_2==l_1:
    print("you win 1000")
else :
    print("sorry")
