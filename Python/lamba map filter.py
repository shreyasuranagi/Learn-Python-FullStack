'''
#lambda
add = lambda a,b: a+b
print(10,20)

even_odd =  lambda num: num**2 if num%2==0 else num**3
print(even_odd(10))
'''

#map
'''
 #to square every no in iterable without loops
l=[1,2,3,4]
square = lambda n: n**2
out=map(square,l)
print(out)
print(list(out))
'''

#filter
'''
l=[1,2,3,4,5,6]
even=lambda x:x%2==0

out=filter(even,l)
print(out)
print(list(out))
'''

'''
#comprehension
a = [3 for i in (1,2,3)]
print(a)

a = [3*2 for i in (1,2,3)]
print(a)


a= [ 3*5 for i in (1,2,3) if i%2==0 ]
print(a)

a=[ 'even' if i%2==0 else 'odd' for i in (1,2,3,4,5,6) ]
print(a)
'''




#advance python

'''
#lambda
#annoymous functions

#syntax 1 - returns an expression
res=lambda a: a+10
print(res)   #<function <lambda> at 0x0000025D01BC0860>

res(10)
print(res(12))

def add(a,b):
    return a+b
print(add(10,20))


add = lambda a,b: a+b
print(add(10,20))

even=lambda n: n%2==0
print(even(34))
print(even(21))


#syntax 2 - with if else condition

#if even square it, if odd then cube it

res = lambda n: n**2 if n%2==0 else n**3
print(res(3)) #27
print(res(2)) #4

#reverse a string
rev = lambda s: s[::-1]
print(rev('password'))

#palindrome
pal = lambda s: s==s[::-1]
print(rev('laal'))

#min and max no of arguments
add = lambda a,b,c=0,d=0,e=0: a+b+c+d+e
#print(add(1))
print(add(2,3))
print(add(1,2,3,4)) #10

#keyword args?
add = lambda a,b: a+b
print(add(b='a',a='b'))

#varialbel length args
add = lambda *args: len(args)
print(add(1,2,3,4,5,6,7,8))
'''

###############
'''
#MAP

def square(l):
    s=[]
    for i in l:
        s.append(l[i])
    print(s)
square([1,2,3])



m = map(lambda n:n**2, [1,2,3])
print(m)
#print(str(m)) #ssam e a sabove
print(tuple(m))
print(list(m)) #cos funciton is called once -> onc eonly output - better to immediately type cast it when createdd
print(tuple(m))

print(set(m))
print(str(m))
print(dict(m))
'''

'''
#m = list(map(lambda n:n**2, eval(input())))
#print(m)

#if eval doesnt work ->

#find lenght of words in a list
l=['hii','bye','say bye']
print(list(map(len,l)))

#find ascii of chars
l=['a','b','c']
print(list(map(ord,l)))

#IMPORTANT - to take input wihtout eval
#how to take input without eval
s='1 23 4 5 6 23'
#l=(list(map(int,s.split())))
l=(list(map(int,input().split())))
print(l)
print(type(l))

#palindrome
l=list(map(lambda w: w[::-1],['abc','e']))
print(l)
'''

#filter
'''
#print(filter(lambda : n+1 if n==0 else n, [1,5,2,0,2,0,0,0]))

#print(list(filter(lambda n: n+1 if n==0 else n, [1,5,2,0,2,0,0,0])))

#extract only int
l=[10,'hi',3.2,20,90]
print(list(filter(lambda i : type(i)==int, l)))

#extract only uppercase from
s=['abc',"ABC",'HELLo','HEYY']
print(s)
#print(list(filter(str.isupper(),s))) #error
print(list(filter(str.isupper,s)))
print(list(filter(str.islower,s)))

print(list(filter(lambda n: n%2==0, [1,2,3,4])))

#wap to find a square of all the even integers present in a list
'''


print( list(map(lambda n: n**2,list(filter(lambda n: type(n)==int and n%2==0 ,[1,3.4,'hi',2,5,6,[1100,900]] )))))




