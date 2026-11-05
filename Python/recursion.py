
#RECURSION
'''
#without recursion
l=[1,2,[4,5,(9,8,{12,43,(9,11,17),35},12,18],19,89],66,1,5]
def add_nested(l):
    s=0
    for i in l:
        if type(i) in [list,set,tuple]:
            ss=0
            for j in l [list,set,tuple]:
            ss=0
            ....
            ....
            .......
        else:
            s=s+i    
add_nested(l)
'''

#with recursion
'''
l=[1,2,[4,5,(9,8,{12,43,(9,11,17),35},12,18),19,89],66,1,5]
#s=0 error
def sum_int(l,s=0):
    
    for i in l:
        if type(i)==int:
            s=s+i
        elif type(i) in [list, set, tuple]:
            s=s+sum_int(i,s)
    return s
print(sum_int(l))
'''

#factorial
'''
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(4))
'''



#sum of  natural numbers
'''
def add(n,s=0,i=0):
    if i>n:
        return s
    s=s+i
    return add(n,s,i=i+1)

print(add(5))

'''

#reverse a number
'''
def reverse(n,rev=0):
    if n<=0:
        return rev
    d=n%10
    rev=rev*10+d
    n=n//10
    return reverse(n,rev)
print(reverse(132))
'''    

#reverse of string using recursion
'''
def rev(s):
    if s=='':
        return
    else:

        return rev()

print(rev('abcd'))
'''

'''
def reverse(s,rev='',i=0):
    if i>=len(s):
        return rev
    rev=s[i]+rev
    return reverse(s,rev,i=i+1)
print(reverse('abcd'))
'''


#1 2 3 4 5 4 3 2 1

def mirror(n, i=1):
    if i>n:
        return 
    print(i,sep=' ',end=' ')
    mirror(n,i=i+1)
    if i!=n:
        print(i,sep=' ',end=' ')


mirror(5)

