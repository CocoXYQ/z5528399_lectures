# In-class Ex 1#
from numpy.ma.core import append

tic='''John said:"Let's learn Python together".'''
print(tic)

x = str('abc')
xup = str.upper(x)
print(xup)

y = 'abc'.upper()
print(y)

"Hi".center(40)
"Hi".center(40,'-')


 a=1
 b=2
 print(f"the value of a is {a} b is {b}")

print("the value of a is {} b is {}".format(a,b))

str= 'nicly done'
str(6)
del(str)
str(6)


#in-class Exercise 2#

length = 56
width = 33
height = 30.5

volume = length * width * height
print(volume)

# constant Var use Capital#

# empty lists#
lst_a = []
Lst_b = list()

# index start with 0, end index will not include
 lst = ["a","b","c","d","e","f"]

 print(lst[2:5])
 print(lst[ : ])
 print(lst[-4:-1])

 lst = [1,"string", True, None,True]
 lst.remove(True)
 print(lst)

 True == 1
 False==0


 line = " welcome to the class"
 x = line.split()
 print(x)

 #in-class EX3# get the domain name unsw.edu.au

line = 'From firstname.surname@unsw.edu.au Mon Sep 16 10:10:15 2024'
x = line.split()
print(x)
newline = x[1]
print(newline)
y= newline.split('@')
print(y[1])
##answer
print(line.split()[1].split('@')[1])

#set doesnt have order 3,2,1 = 1,2,3

# list - mutable, ordered  ## [] or list ()
# tuple -  unmutable, ordered ## () or tuple()
#set -  mutable unordered, no duplicate only set()
#dic - mutable unordered, key-value pair {} or dict()

