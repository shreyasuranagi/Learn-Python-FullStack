'''
def reverse(n,rev=0,i=0):
    if n<=0:
        return rev
    d=n%10
    rev=rev*10+d
    n=n//10
    return reverse(n,rev,i=i+1)
print(reverse(65321))
'''

'''
def reverse(s,i=0,rev=''):
    if i==len(s):
        return rev
    rev=s[i]+rev
    return reverse(s,i+1,rev)
print(reverse('abc'))
'''

'''
n=int(input('Enter:'))
i=0
a=0
b=1
if n==1:
    print(0)
elif n==1:
    print(0,1)
elif n>2:
    print(a,b,end=' ')
    while i<=n-2:
        c=a+b
        print(c,end=' ')
        a=b
        b=c
        i=i+1
'''

'''

def mirror(n,i=0):
    if i==n:
        print(i,end=' ')
        return
    print(i,end=' ')
    mirror(n,i+1)
    print(i,end=' ')
n=int(input('Enter:'))
mirror(n)
'''

'''
s=input('Enter a sentence:')
word_list=s.split()
out=[]
for word in word_list:
    out.append(word[::-1])
out=' '.join(out)
print(out)
'''

'''
n=int(input('Enter:'))
i=1
s=0
while i<=n//2:
    if n%i==0:
        s+=i
    i+=1
if s==n:
    print(n,' is a perfect number')
else:
    print(n,' is NOT a perfect numner')
'''

'''
#fibonacci using recursion

def fib(n):
    if n==1:
        return 0
    if n==2:
        return 0,1

'''
'''
    
