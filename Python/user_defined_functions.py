# without arguments -> take user inputs inside function only OR we dont need to work on any inputs
# without return -> print output inside function only, when we DONt need to use outputs again 
# with arguments -> user inputs are taken OR were already taken OUTSIDE the function, just pass it so func can use it
# with return -> send final output value, AND we must print the function call itself : print(fname(..))
                    # OR assign function call to variable OR multiple var assignment fo multiple values returned


# FUNCTION TYPE 1
#1. functions without arguments and without return
'''

def sum():
    a=int(input('Enter:'))
    b=int(input('Enter:'))
    print('sum:',a+b)
    
sum()
'''


#wap to reverse a string using function type 1
'''
def reversestr():
    
    s=input('Enter:')
    rev=''
    for c in s:
        rev=c+rev
    print(rev)

reversestr()
'''

'''
    s=input('Enter:')
    rev=''.join(list(reversed(s)))
    print(rev)
    '''

#2. functions with arguments and without return
'''
def add(n1,n2):
    print(n1+n2)
    
add(10,400)
add('abc','a3')
add(3.5,9)
add([1,2],[2,4])
'''

#wap to find the factorial of a number
'''
def factorial(n):
    i=1
    prod=1
    while i<=n:
        prod=prod*i
        i+=1
    print(prod)
factorial(5)

add(2,3)
'''


#3. functions without arguments and with return
'''
def sam():
    n1=int(input('Enter:'))
    n2=int(input('Enter:'))

    return n1+n2,n1-n2  #?

a,b=sam()
print(a,b)
print('-'*5)
print(sam())
print('-'*5)
c=sam()
print(c)

'''

#4. functions with arguments and with return
'''
def sam(n1, n2):

    return n1+n2,n1-n2
print(sam(10,20))
c=sam(10,20)
x,y=sam(10,20)
print(c)
print(x,y)
'''


#wap to check whether number is prime or not
'''
def prime_check():
    n=int(input('Enter:'))
    i=1
    count=0
    while i<=n//2:
        if count>1:
            break
        if n%i==0:
            count+=1
        i+=1
    return count

s=prime_check()
if s==1:
    print('Prime')
else:
    print('Not prime')
'''

'''
#more efficient
def prime_check():
    n=int(input('Enter:'))
    for i in range(2,n): #or n**0.5
        if n%i==0:
            return n,'is prime'
    return f'{n} is not prime'

print(prime_check())
'''


#Assignment
#121.Wap to check whether the number is strong or not. - 145-1!+4!+5!

#function type1

#def fact():
'''
def is_strong():
    n=int(input('Enter:'))
    num=n
    s=0
    while n>0:
        d=n%10
        prod=1
        for i in range(1,d+1):
            prod=prod*i
        s=s+prod
        n=n//10
    if s==num:
        print(f'{num} is a strong number')
    else:
        print(f'{num} is not a strong number')
        
is_strong()
'''

#function type2
'''
def is_strong(n):
    num=n
    s=0
    while n>0:
        d=n%10
        prod=1
        for i in range(1,d+1):
            prod=prod*i
        s=s+prod
        n=n//10
    if s==num:
        print(f'{num} is a strong number')
    else:
        print(f'{num} is not a strong number')

n=int(input('Enter to check for strong no:'))
is_strong(n)
'''

#function type3
'''
def is_strong():
    n=int(input('Enter:'))
    num=n
    s=0
    while n>0:
        d=n%10
        prod=1
        for i in range(1,d+1):
            prod=prod*i
        s=s+prod
        n=n//10
    if s==num:
        return f'{num} is a strong number'
    else:
        return f'{num} is not a strong number'

print(is_strong())
'''

#q 122.Wap to print the strong numbers between the given range.

#function type 1
'''
def print_strong():
    start=int(input('Enter start of range:'))
    end=int(input('Enter end of range:'))
    print(f'strong numbers in the range {start} to {end} are:')
    for i in range(start, end+1):
        num=i
        s=0
        while i>0:
            d=i%10
            prod=1
            for j in range(1,d+1):
                prod=prod*j
            s=s+prod
            i=i//10
        if s==num:
            print(num)
        
print_strong()
'''


#function type 2
'''
def print_strong(start, end):
    print(f'strong numbers in the range {start} to {end} are:')
    for i in range(start, end+1):
        num=i
        s=0
        while i>0:
            d=i%10
            prod=1
            for j in range(1,d+1):
                prod=prod*j
            s=s+prod
            i=i//10
        if s==num:
            print(num)

start=int(input('Enter start of range:'))
end=int(input('Enter end of range:'))        
print_strong(start,end)
'''

#function type 3 - no args only return
'''
def print_strong():
    start=int(input('Enter start of range:'))
    end=int(input('Enter end of range:'))
    for i in range(start, end+1):
        num=i
        s=0
        while i>0:
            d=i%10
            prod=1
            for j in range(1,d+1):
                prod=prod*j
            s=s+prod
            i=i//10
        if s==num:
            return(num) #stops execution
print(print_strong())
'''

#q 123.Wap to find the nth strong number.

#function type 1
'''
def nth_strong():
    n=int(input('Enter:'))
    count=0
    i=1
    while True:
        num=i
        s=0
        while num>0:
            d=num%10
            #fact
            fact=1
            for j in range(1,d+1):
                fact=fact*j
            s=s+fact
            #add the fact
            num=num//10
        if s==i:
            count+=1
            if count==n:
                print(i)
                break
        i=i+1
      
nth_strong()

'''

# function type 2
'''
def nth_strong(n):
    
    count=0
    i=1
    while True:
        num=i
        s=0
        while num>0:
            d=num%10
            #fact
            fact=1
            for j in range(1,d+1):
                fact=fact*j
            s=s+fact
            #add the fact
            num=num//10
        if s==i:
            count+=1
            if count==n:
                print(i)
                break
        i=i+1
n=int(input('Enter:'))      
nth_strong(n)
'''

#function type 3
'''
def nth_strong():
    n=int(input('Enter:')) 
    count=0
    i=1
    while True:
        num=i
        s=0
        while num>0:
            d=num%10
            #fact
            fact=1
            for j in range(1,d+1):
                fact=fact*j
            s=s+fact
            #add the fact
            num=num//10
        if s==i:
            count+=1
            if count==n:
                return(i)
                break
        i=i+1
     
print(nth_strong())
'''

#q 124.Wap to check whether the number is arm strong or not

#function type1
'''
def is_armstrong():
    n=int(input('Enter:'))
    
    #find no of digits
    temp=n
    count=0
    while n>0:
        d=n%10
        count+=1
        n=n//10
    

    #check for armstrong - sum (digits'cube)

    num=temp
    s=0
    while num>0:
        d=num%10
        s=s+d**count
        num=num//10

    if s==temp:
        print(f'{temp} is an armstrong number')
    else:
        print(f'{temp} is NOT an armstrong number')
is_armstrong()
'''

#function type2
'''
def is_armstrong(n):
    
    
    #find no of digits
    temp=n
    count=0
    while n>0:
        d=n%10
        count+=1
        n=n//10
    

    #check for armstrong - sum (digits'cube)

    num=temp
    s=0
    while num>0:
        d=num%10
        s=s+d**count
        num=num//10

    if s==temp:
        print(f'{temp} is an armstrong number')
    else:
        print(f'{temp} is NOT an armstrong number')
n=int(input('Enter:'))
is_armstrong(n)
'''


#function type 3
'''
def is_armstrong():
    n=int(input('Enter:'))
    #find no of digits
    temp=n
    count=0
    while n>0:
        d=n%10
        count+=1
        n=n//10
    
    #check for armstrong - sum (digits'cube)

    num=temp
    s=0
    while num>0:
        d=num%10
        s=s+d**count
        num=num//10

    if s==temp:
        return(f'{temp} is an armstrong number')
    else:
        return(f'{temp} is NOT an armstrong number')

print(is_armstrong())
'''

#q126.Wap to find the nth arm strong number

#function type 1
#trial
'''
def nth_armstrong():
    n=int(input('Enter nth value:'))
    num=1
    count=0
    print('count',count)
    while True:
        print()
        print('===')
        print('no now:',num)
        temp=num
        dig_count=0
        print('dig_count',dig_count)
        while temp>0:
            d=temp%10
            dig_count+=1
            print('dig_count',dig_count)
            temp=temp//10

        temp=num
        print('no now:',temp)
        s=0
        print('sum before',s)
        while temp>0:
            d=temp%10
            print('power',d**dig_count)
            s=s+d**dig_count
            print('sum in loop',s)
            temp=temp//10
        print('sum after',s)
        if s==num:
            
            count+=1
            print('couunt',count)
            if count==n:
                
                print(s,' is the ',n,'th armstrong number')
                break

        num+=1
    
nth_armstrong()       
'''

#final
'''
def nth_armstrong():
    n=int(input('Enter nth value:'))
    num=1
    count=0
    while True:
        temp=num
        dig_count=0
        while temp>0:
            d=temp%10
            dig_count+=1
            temp=temp//10

        temp=num
        s=0
        while temp>0:
            d=temp%10
            s=s+d**dig_count
            temp=temp//10
        if s==num:
            count+=1
            if count==n:
                print(s,' is the ',n,'th armstrong number')
                break
        num+=1
    
nth_armstrong()  

'''

#functipn type 2 - no return with arg
'''
def nth_armstrong(n):
    
    num=1
    count=0
    while True:
        temp=num
        dig_count=0
        while temp>0:
            d=temp%10
            dig_count+=1
            temp=temp//10

        temp=num
        s=0
        while temp>0:
            d=temp%10
            s=s+d**dig_count
            temp=temp//10
        if s==num:
            count+=1
            if count==n:
                print(s,' is the ',n,'th armstrong number')
                break
        num+=1

n=int(input('Enter nth value:'))    
nth_armstrong(n) 
'''


#function type 3
'''
def nth_armstrong():
    n=int(input('Enter nth value:'))    
    num=1
    count=0
    while True:
        temp=num
        dig_count=0
        while temp>0:
            d=temp%10
            dig_count+=1
            temp=temp//10

        temp=num
        s=0
        while temp>0:
            d=temp%10
            s=s+d**dig_count
            temp=temp//10
        if s==num:
            count+=1
            if count==n:
                #return (s,' is the ',n,'th armstrong number')
                return f'{s} is the {n}th armstrong number'
                break
        num+=1


print(nth_armstrong())
'''



