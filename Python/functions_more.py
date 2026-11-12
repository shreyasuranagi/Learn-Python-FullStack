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
















