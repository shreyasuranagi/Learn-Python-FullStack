#wap to print hello 5 times
'''
s='hello'
i=1
while i<=5:
    print(s)
    i=i+1
'''

#wap to print numbers from 1 to 10
'''
i=1
while i<=10:
    print(i)
    i+=1
'''

#wap to print numbers from 10 to 1
'''
i=10
while i>=1:
    print(i)
    i=i-1
'''

#wap to print the even numbers between 1 to n
'''
n=int(input("Enter a number:"))
i=1 
while i<=n:
    if i%2==0: 
        print(i)
    i+=1
'''

'''
#more efficient-iterations are decreased
n=int(input("Enter a number:"))
i=2
while i<=n:
    print(i)
    i+=2
'''


#wap to print the factors of a number
#factors start form 1 and always less than n
'''
n=int(input("Enter a number to find the factors of:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i=i+1
'''

'''
#more efficient - reduces no of iterations
n=int(input("Enter a number to find the factors of:"))
i=1
while i<=n/2:
    if n%i==0:
        print(i)
    i=i+1
print(n)
'''
    
#wap to find the sum of n natural numbers
'''
n=int(input("Enter a number to find n natural numbers:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum of",n,"natural numbers is",sum)
'''

#wap to find the product of n natural numbers/factorial of a number
'''
n=int(input("Enter number to find factorial of number:"))
prod=1
i=1 #or i=2
while i<=n:
    prod=prod*i;
    i=i+1
print("Factorial of",n,"is",prod)
'''

#wap to print multiplication table of a given program
'''
n=int(input("Enter no. to print the multiplication table of:"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i=i+1
'''

#wap to find the sum of even numbers 1 to 100
'''
sum=0
i=2
while i<=100:
    sum=sum+i
    i=i+2
print("Sum of even nos 1 to 100:",sum)

'''
#wap to print the product of odd numbers between 1 to 50
'''
prod=1
i=1
while i<=50:
    prod=prod*i
    i=i+2
print("Product of odd numbers 1 to 50:",prod)

'''
#wap to check whether a number is perfect number or not
'''
n=int(input("Enter a number:"))
sum=0
i=1
while i<=n/2:
    if n%i==0:
        sum=sum+i
    i+=1

if sum==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
'''


#wap to count the number of digits present in a number (w/o len function)
'''
num=int(input("Enter a nummber to count the digits of:"))
count=1
n=1
while n*10<=num:
    count=count+1
    n=n*10
print("Number of digits:",count)

'''

#wap to print the sum of all digits of a number
'''
n=int(input("Enter a number to find the sum of digits:"))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print("Sum of digits is:",sum)

#or
n=int(input("Enter:"))
count=0
while


'''

#wap to reverse a number
'''
n=int(input("Enter a number to print the reverse:"))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("reverse of number:",rev)

##or
'''

#wap to check if palindrome
'''
n=int(input("Enter a number to print the reverse:"))
rev=0
temp=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
    print("Palindrome",rev,"=",temp)
else:
    print("Not palindrome",temp,"!=",rev)
'''

#wap to convert an int to binary
'''
n=int(input("Enter an integer to convert to binary:"))
binary=0
power=0
while n>0:
    d=n%2
    binary=d*10**power+binary
    n=n//2
    power=power+1
print(binary)
'''

#wap to convert binary to int
'''
n=int(input('enter a binary no to convert to int:'))
power=0
bi=0
while n!=0:
    d=n%10
    bi=d*2**power+bi
    n=n//10
    power+=1
print(bi)
'''


# wap to extract the char present at even index
'''
s=input('Enter a string to extract chars from even index:')
i=0
ems=''
while i<=len(s)-1:
    if i%2==0:
        ems=ems+s[i]
    i=i+1
print('String after extracting at even index:',ems)

#OR use i+=2 isntead of i%2==0
'''

# wap to extract the vowels present in a string
'''
s=input('Enter a string to extract the vowels from:')
i=0
vow_string=''
while i<=len(s)-1:
    if s[i] in 'aeiouAEIOU':
        vow_string = vow_string + s[i]
    i=i+1
print('extracted vowel string:',vow_string)
'''

# wap to get the following output:
# s1='00110101101'
# s2='01011010101'
# out=5
'''
#can be done directly

print('Program to count no of similar character occurring at similar positions')
s1=input('Enter string 2:')
s2=input('Enter sring 1:')
i=0
count=0
while i<=len(s1)-1 and i<=len(s2)-1:
    if s1[i]==s2[i]:
        count=count+1
    i=i+1
print("Count:",count)

#OR use minimum length
'''

# wap to replace the space present in a string by *
'''
s=input('enter:')
i=0
new_str=''
while i<=len(s)-1:
    if s[i]==' ':
        new_str=new_str+'*'
    else:
        new_str=new_str+s[i]
    i=i+1
print('New string:',new_str)
'''

# wap to check whether the number is armstrong or not
'''
n=int(input('enter a number to check for armstrong number:'))
num=n
n1=n
arm=0
##to find digits
count=0
while n!=0:
    d=n%10
    count+=1
    n=n//10

while num!=0:
    d=num%10
    arm=arm+d**count
    num//=10

if n1==arm:
    print('armstrong',arm,n1)
else:
    print('not armstrong',arm,n1)
'''
#OR
n=int(input("enter:"))
temp=n
sum=0
l=len(str(n))
while n>0:
    d=n%10
    sum+=d**l
    n=n//10
if temp==sum:
    print(temp,'is armstrong number')
else:
    print(temp,'is not an armtstrong number')

    


