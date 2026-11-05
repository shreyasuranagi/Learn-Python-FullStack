#method overloading not supported
#by default python does method overrriding
'''
def sam(a,b):
    print(a+b)
def sam(a,b,c):
    print(a+b-c)
def sam(a,b,c,d):
    print(a+b,c-d)

#sam(10,20) #TypeError: sam() missing 2 required positional arguments: 'c' and 'd'

'''

#assigning function to the variable
#
'''
def sam(a,b):
    print(a+b)
temp1=sam
def sam(a,b,c):
    print(a+b-c)
temp2=sam
def sam(a,b,c,d):
    print(a+b,c-d)

sam(1,2,3,4)
temp1(10,20)
'''


#method overriding
'''
class Parent:
    def sam(self):
        print('Im from Parent class')

ob1=Parent()
ob1.sam()

class Child(Parent):
    def sam(self):
        print('IM from child class')
    
    
    def hello(self):
        print('hello everyone')
ob=Child()
ob.sam()
ob.hello()
'''


#duck typing -
'''
class Dog:
    def sound(self):
        print('bow bow')

class Cat:
    def sound(self):
        print('meow meow')

d=Dog()
c=Cat()

def make_sound(obj):
    obj.sound()
'''


#operator overloading
'''
class Sam:
    def __init__(self,num):
        self.num=num

    def __add__(self,other):
        return self.num+other.num

    def __mul__(self,other):
        return self.num*other.num

    def __sub__(self,other):
        return self.num-other.num

    def __truediv__(self,other):
        return self.num/other.num

    def __floordiv__(self,other):
        return self.num//other.num

    def __mod__(self,other):
        return self.num%other.num

    def __pow__(self,other):
        return self.num**other.num
    def __str__(self):
        return "<class 'Sam'>"

    def __call__(self):
        return "object is being called"
        
x=Sam(10)
print(x)
print(x.num)
print(type(x))

y=Sam(20)
print(y)
print(y.num)
print(type(y))

print('sum:',x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)
print()
print(x)
print(x())

'''

#RELATIONAl

#Operator overloading assignment -Relational operators

class Relational:
    def __init__(self,a):
        self.a=a
    def __eq__(self,other):
        return self.a==other.a
    def __lt__(self,other):
        return self.a<other.a
    def __gt__(self,other):
        return self.a>other.a
    def __le__(self,other):
        return self.a<=other.a
    def __ge__(self,other):
        return self.a>=other.a
    def __ne__(self,other):
        return self.a!=other.a
    def __str__(self):
        return "<class 'Relational'>"
    def __call__(self):
        return "object is being called"
    

a=Relational(10)
b=Relational(20)

print(type(a))
print(a)
print(a())
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)



a=Relational('abc')
b=Relational('abd')


print(type(a))
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)



#BITWISE

    


class Bitwise:
    def __init__(self,a):
        self.a=a
    def __and__(self,other):
        return self.a&other.a
    def __or__(self,other):
        return self.a|other.a
    def __xor__(self,other):
        return self.a^other.a
    def __invert__(self):
        return ~self.a
    def __lshift__(self,n):
        return self.a<<n
    def __rshift__(self,n):
        return self.a>>n

a=Bitwise(13)
b=Bitwise(-5)
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<3)
print(b>>2)





