#wap to remove duplicates form a list
'''
def remove_dup(l):
    out_l=[]
    for i in l:
        if i not in out_l:
            out_l.append(i)

    return out_l


#print(remove_dup(eval(input('Enter a list:')))) #more efficient
#print(remove_dup((1,2,3,2)))
'''

#wap to check whether the number is perfect number or not
#6 = 1+2+3 sum of factors
'''
def is_perfect(n):
    s=0
    i=1
    while i<=n//2+1:
        if n%i==0:
            s=s+i
    
        i+=1
    
    return s==n #efficient less loc
#optional below
if is_perfect(int(input('Enter:'))):
    print('perfect')
else:
    print('not perfect')
'''

#wap to check whether a number is a storng number or not
#145 = 1! + 4! + 5!
'''
def is_strong(n):
    temp=n
    s=0
    while n>0:
        d=n%10
        prod=1
        for i in range(1,d+1):
            prod=prod*i
        s=s+prod
        n=n//10

    return s==temp

print(is_strong(int(input('Enter:'))))
'''
#OR
'''
def is_strong2(n):
    s=0
    temp=n
    for d in str(n):
        fact=1
        for i in range(1,int(d)+1):
            fact*=i
        s=s+fact
    return s==temp
print(is_strong2(int(input('Enter:'))))
'''
'''
#using nested function
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    
    return fact


def is_strong3(n):
    temp=n
    s=0
    for d in str(n):
        s=s+factorial(int(d))
    return s==temp
print(is_strong3(14))

'''




#q what is the significance of usign funcitosn wiht argumenta nd returns
#q how come NOne is returned?
#q what happens actulaly callign afucntion with mroe or less params how s ite checked
#q cant enforce data type chack in params?

#wap to print the strong numbers between 1 to 10000
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    
    return fact

def is_strong3(n):
    temp=n
    s=0
    for d in str(n):
        s=s+factorial(int(d))
    return s==temp

def strong_number():
    for i in range(1,50000+1):
        if is_strong3(i):
            print(i)
'''    

#wap to print the prime numbers between 1 to 10000
'''
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def prime_numbers():
    for i in range(1,1001):
        if is_prime(i):
            print(i)
prime_numbers()        
'''           
#wap to print the perfect numbers between 1 to 10000
'''
def is_perfect(n):
    
    s=0
    i=1
    while i<n: #n//2
        if n%i==0:
            s=s+i
    
        i+=1
    
    return s==n #efficient less loc

def perfect_numbers():
    for i in range(1,1001):
        if is_perfect(i):
            print(i)
perfect_numbers()        

'''
#wap to print the armstrong numbers between 1 to 10000
'''
def is_armstrong(n):
    temp=n
    num=n
    count_d=0
    while n>0:
        d=n%10
        count_d+=1
        n=n//10

    s=0
    while num>0:
        d=num%10
        s=s+d**count_d
        num=num//10

    return s==temp 


def armstrong_numbers():
    for i in range(1,10000+1):
        if is_armstrong(i):
            print(i)



armstrong_numbers()
'''




# wap to print 139.Wap to check whether the number is happy number or not
# A Happy Number is a positive integer that eventually reaches 1 when you repeatedly replace it with the sum of the squares of its digits.
# • \(1^2 + 9^2 = 1 + 81 = 82\)
# • \(8^2 + 2^2 = 64 + 4 = 68\)
# • \(6^2 + 8^2 = 36 + 64 = 100\)
# • \(1^2 + 0^2 + 0^2 = 1\) (Happy!)
'''
n=int(input('Enter a no to check if it is happy or not:'))

while n>=10:

    temp=n
    s=0
    while temp>0:
        
        d=temp%10
        
        s=s+d**2
        
        temp=temp//10
    n=s

if s==1:
    print('happy number')
else:
    print('not happy')
'''



#144.Wap to check whether the number is xylem or not.
#Ex: 1234→1+4=2+3
#The sum of the first and last digits equals the sum of the middle digits

#single digit-true
#two digit - false
#first (n//10) + last(n//10**len(n) == loop len(n)-2 times starting from n//100)

'''
def is_xylem():
    n=int(input('Enter:'))
    l=len(str(n))
    if n//10==0:
        return True
    elif n//100==0:
        return False
    else:
        lh=n%10 + (n//(10**(l-1)))
        print(n%10)
        print((n//(10**(l-1))))
        print(lh)
        i=l-2
        rh=0
        n=n//10
        while i>0:
            d=n%10
            rh=rh+d
            n=n//10
            i=i-1
        print(rh)
        if lh==rh:
            return True
        else:
            return False

print(is_xylem())
'''


'''
def is_xylem():
    n=int(input('Enter:'))
    if n//10==0:
        return True
    elif n//100==0:
        return False 
    else:
        lh = 0
        lh = lh + n%10
        print(lh)
        n=n//10
        rh=0
        while n>0:
            print(n)
            d=n%10
            rh=rh+d
            if n//100==0:
                lh=lh+(n//10)%10
                break
            n=n//10
        if lh==rh:
            return True
        else:
            return False
        
print(is_xylem())

'''



'''
# 145.Wap to check whether the number is spy or not.
#  Ex: 123→1+2+3=1*2*3
def spy():
    n=int(input('Enter:'))

    sum=0
    prod=1

    while n>0:
        d=n%10
        sum=sum+d
        prod=prod*d
        n=n//10
    if sum==prod:
        print('Spy number')
    else:
        print('Not a spy number')
spy()
'''


'''
# 142.wap to check whether the string is anagram or not.
# listen=silent

s1=input('Enter string s1:')
s2=input('Enter string s2:')
a1=sorted(s1)
a2=sorted(s2)
if a1==a2:
    print('Anagrams')
else:
    print('Not anagrams')
'''


'''
#check
s1=input('Enter string s1:')
s2=input('Enter string s2:')

for ch in s1:
    if ch in s2:
        s2=s2.replace(ch,'')
        s1=s1.replace(ch,'')

if s2=='':
    print('Anagrams')
else:
    print('Not anagrams')
'''

'''
#  143.Wap to check whether the string is pangram or not.
# it has every alphabet of English at least once
# eg - the quick brown fox jumps over the lazy dog
s='the quick brown fox jumps over the lazy dog'
alpha='abcdefghijklmnopqrstuvwxyz'
for ch in s.lower():
    if ch in alpha:
        alpha=alpha.replace(ch,'')
if alpha=='':
    print('pangram')
else:
    print('not a pangram')
'''








