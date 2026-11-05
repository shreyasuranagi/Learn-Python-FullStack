
##############################

#simple - if

#q1.wap to print square of a int number if it is even
'''
num=int(input("enter:"))
if num%2==0:
    print(num,"is even and its square is",num**2)
'''

#q2. wap to check whether char is vowel or not
'''
cin=input('Enter a single character')
if cin=='a' or cin=='e' or cin=='i'or cin=='o' or cin=='u' or cin=='A' or cin=='E' or cin=='I' or cin=='O' or cin=='U':
    print("It is  a vowel")


cin=input('Enter a single character:')
if cin in 'aeiouAEIOU':
    print(cin,"is a vowel")
'''

#q3. wap to print the ascii value of a character only if it is upper case
'''
c=input('Enter a char:')
if 'A'<=c<='Z':
    print(ord(c))
'''

#q4. wap to print the cube of a number only if it is divisible by 9 or 6
'''
n=int(input('enter to check divisibility by 9 or 6:'))
if n%9==0 or n%6==0:
    print(f"Cube of {n} is {n**3}")
'''


#q5. Wap to check whether the given integer is 3 Digit number.
'''
n=int(input('Enter to check whether digit is 3 digit:'))
if len(str(n))==3:
    print('it is a 3 digit number')
'''

#q6. Wap to check whether the last digit of a given number is 5.
'''
n=int(input('Enter a no. to check its last digit is 5:'))
if n%10==5:
    print('last digit is 5')
'''
    

#q7. Wap to check whether the given data is float.
'''
n=input('Enter a number to check if its float')
if type(n)==float:
    print('It is float')
'''


    
#q8. Wap to check whether the data is single value data.
'''
n=eval(input('Enter to check if is SVD:'))
if type(n)==float or type(n)==int or type(n)==bool or type(n)==complex:
    print("It is a single value data")
'''


#q9. wap to check whether character is digit or not
'''
ch=input("Enter a single character:")
if ch>='0' and ch<='9':
    print(ch,"is a digit")
else:
    print(ch,"is not digit")
'''

#q10.Wap to check whether the given integer is multiple of 3.
'''
n=int(input('Enter a no to check if it is multiple of 3'))
if n%3==0:
    print('It is a multiple of 3')
'''

##########################

#if-else

#q11. wap to check whether data is mutable or not
'''
d=eval(input("Enter any data to check mutable: "))
#if type(d)==type([]) or type(d)==type(set()) or type(d)==type({}):
if type(d) in [list,set,dict]:
    print("it is mutable")
else:
    print("it is not mutable")
'''

#q12. wap to check whether character is digit or not
'''
ch=input("Enter a single character:")
if ch>='0' and ch<='9':
    print(ch,"is a digit")
else:
    print(ch,"is not digit")
'''



#q13. wap to check whether the given char is special or not
'''
ch=input("Enter a character:")
if not('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'):
    print(f"{ch} it is a special character")
else:
    print(f"{ch} it is not a special character")

'''
#q14. wap to check whether list contains middle value or not
'''
l=eval(input("enter:"))
print("length of list:",len(l))
if len(l)%2==1:
    print("there is a single middle value",end="--")
    print("the middle value is:",l[int(len(l)/2)]) #l[len(l)//2]
else:
    print("there is no middle value")
'''

#q15. wap to check whether the no is even or odd
'''
n=int(input('Enter a no.:'))
if n%2==0:
    print('it is even')
else:
    print('it is odd')
'''

#q16. wap to check whether data is mutable or immutable
'''
d=eval(input("Enter any data to check mutable: "))
#if type(d)==type([]) or type(d)==type(set()) or type(d)==type({}):
if type(d) in [list,set,dict]:
    print("it is mutable")
else:
    print("it is not mutable")
'''

#q17. wap to check whether 2 vlaues pointing to same memory or not
'''
x=eval(input("enter:"))
y=eval(input("enter:"))
#if id(x)==id(y):
if x is y:
    print("pointing to same memory")
else:
    print("not pointing to same memory")

'''

#q18.Consider a tuple of length 2 and check whether the tuple is homogenous or not
'''
t=eval(input('Enter a tuple:'))
if type(t[0])==type(t[1]):
    print('It is a homogeneous')
else:
    print('It is not homogeneous')
'''

#q19. wap to check whether string is palindrome or not
'''
s=int(input("Enter a string to check palindrome:"))
if s==s[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome {s[::-1]}")
'''


#q20. wap to check whether number is positive or negative
'''
n=int(input('enter a number:'))
if n>=0:
    print('it is positive')
else:
    print('it is negative')
'''

##############################


#elif

#q21. wap to check whether  char is uppe,r lower, digit or special
'''
ch=input('Enter a char:')
if 'A'<=ch<='Z':
    print('uppercase')
elif 'a'<=ch<='z':
    print('lowercase')
elif '0'<=ch<='9':
    print('digit')
else:
    print('special character')
'''


#q22. wap to check whether the given integer is single digit or 2 or 3 or or more than 3 digits
'''
n=int(input('enter an integer:'))
if len(str(n))==1:
    print('It is a 1 digit number')
elif len(str(n))==2:
    print('It is a 2 digit number')
elif len(str(n))==3:
    print('It is a 3 digit number')
else:
    print('It is more than 3 digit number')
'''

#q23. wap to check where the point lies on the quadrant
'''
x=int(input("Enter x coordinates:"))
y=int(input("Enter y coordinates:"))

if x==0 and y==0:
    print(f"({x},{y}) is Origin")
elif x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2")
elif x<0 and y<0:
    print("Quadrant 3")
elif x>0 and y<0:
    print("Quadrant 4")
elif x==0 and y!=0:
    print("On y axis")
else:
    print("On x axis")
'''

#q24. wap to find the greatest of 3 numbers
'''
#q. WAP TO FIND the GREATEST of 3 numbers
print("To find greatest of 3 numbers",end="******\n")
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a>=b and a>=c:
    print(f"{a} is the greatest")
elif b>=a and b>=c:   #OR - b>=c
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")
'''

###########
'''
print("To find greatest of 3 numbers",end="******\n")
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if b<=a>=c:
    print(b,'is greater')
elif a<=c>=b:
    print(c,'is greater')
else:
    print(a,'is greater')
'''

###########
'''
print("To find greatest of 3 numbers",end="******\n")
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a==b==d:
    print("all are equal")
if a>b and a>d:
    print(a,'is greater')
elif b>c:
    print(b,'is greater')
else:
    print(c,'is greater')
'''



#q25. wap to find the smallest of 3 numbers
'''
print('To find the smalles number')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
if a<b and a<c:
    print(a,'is smallest')
elif b<c:
    print(b,'is smallest')
else:
    print(c,'is smallest')
'''    
    
#q26 wap to check the relation between 2 integer numbers
'''
print('To find the relation between 2 numbers')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
if a>b:
    print(f'{a} is greater than {b}')
elif a<b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} is equal to {b}')
'''
    
#q27. wap to convert lower to upper, upper to lower, if digit print its remainder divided by 3,
#if it is special print its ascii
'''
c=input('Enter a character:')
if 'a'<=c<='z':
    print(chr((ord(c))-32))
elif 'A'<=c<='Z':
    print(chr(ord(c)+32))
elif '0'<=c<='9':
    print(int(c)%3)
else:
    print('ascii of',c,'is',ord(c))
'''

#q28. fizzbuzz
'''
#q. wap to print fizz if multiple of 3, buzz if multiple of 5 and fizzbuzz if multi of 3 and 5

n=int(input("Enter a number to check for fizzbuzz: "))
if n%3==0 and n%5==0:
    print("Fizzbuzz")
elif n%3==0 and n%5!=0:
    print("Fizz")
elif n%3!=0 and n%5==0:
    print("Buzz")
'''


####################
#nested if


#q29. Wap to login into the Instagram with valid username and password.(enter
# password only if the user name is valid
'''
username='abc'
password='abc123'
print('Login to Instagram:')
u=input('Username:')
if u==username:
    p=input('Password:')
    if p==password:
        print('Logged in successfully')
    else:
        print('Invalid password!')
else:
    print('Invalid username!')
'''

#q30. wap to print the middle value of a list only if it is a string
'''
l=eval(input('Enter a list:'))
if len(l)%2==1:
    if type(l[len(l)//2])==str:
        print(l[len(l)//2])
    else:
        print('middle value is not a string')
else:
    print('there is no middle value in list')
'''


#q31. wap to check whether a character is vowel or consonant
'''
#vowel or consonant
ch=input("Enter a character:")
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    if ch in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonant")
else:
    print("not an alphabet")
'''

#q32.Wap to find the greatest of 4 numbers
'''
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
d=int(input('Enter 4th number:'))

if a>b and a>c and a>d:
    print(a,'is greatest')
elif b>c and b>d:
    print(b,'is greatest')
elif c>d:
    print(c,'is greatest')
else:
    print(d,'is greatest')
'''

#q33.  Wap to print the value as it is only if the length of the value is even.
'''
n=int(input('Enter:'))
if len(str(n))%2==0:
    print(n)
'''

#q34. Wap to print the last value of a list only if it is palindrome string starting with vowel.
'''
l=eval(input('Enter a list:'))
if type(l[-1])==str:
    if l[-1][0] in 'aeiouAEIOU':
        if l[-1]==l[-1][::-1]:
            print(l[-1])
        else:
            print('Not a palindrome')
    else:
        print('Not starting with a vowel')
else:
    print('Not a string')
'''

#q35. Wap to print the reversed string only if it is starting with vowel ,ending with consonant and having a middle value.
'''
s=input('Enter a string:')
if len(s)%2==1:
    if ('a'<=s[0]<='z' or 'A'<=s[0]<='Z') and ('a'<=s[-1]<='z' or 'A'<=s[-1]<='Z'):
        if s[0] in 'aeiouAEIOU':
            if s[-1] not in 'aeiouAEIOU':
                print('Reversed string:',s[::-1])
            else:
                print('not ending with consonant')
        else:
            print('not starting with vowel')
    else:
        print('not starting or ending with alphabet')
else:
    print('it does not have middle value')
'''
#q36. Wap to find the second greatest of 4 values.-?
''' #THIS IS NOT COMPLETED -ONLY ROUGH WORK
print('To find 2nd greatest of 4 numbers')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
d=int(input('Enter 4th number:'))

abcd
b a
a b
c

if a>b:
    if a>c:
        if a>d:
            print(a)
        else:
            print(d)
    elif c>d:
        print(c)
    else:
        print(d)
elif 



if a>=b and a>=c and a>=d:
    print(a)
elif b>=c and


if b>=a or c>=a or d>=a:
    print(a)
elif 
    
if b>=c and b>=d:
    if b>a:
        print(b)
    else:
        print(a)
elif c>=d and c>=a:
    if c>b:
        print(c)
    else:
        print(b

a b c d
'''

#q36. Wap to find the second greatest of 4 values.-?

a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
d=int(input('Enter 4th number:'))
sec=-999
if a>=b and a>=c and a>=d:
    #greatest=a
    if b>=c and b>=d:
        sec=b
    elif c>=d:
        sec=c
    else:
        sec=d
elif b>=c and b>=d:
    #greatest=b
    if a>=c and a>=d:
        sec=a
    elif c>=d:
        sec=c
    else:
        sec=d
elif c>=d:
    #greatest=c
    sec=d
else:
    #greatest=d
    sec=c
print('Second greatest:',sec)


#q37. Wap to find the smallest of 4 numbers.
'''
print('To find smallest of 4 numbers')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
d=int(input('Enter 4th number:'))
print('smallest:',end='')
if a<=b and a<=c and a<=d:
    print(a)
elif b<=c and b<=d:
    print(b)
elif c<=d:
    print(c)
else:
    print(d)
'''

#q38. Write a program to print middle Character of the given string only if it is upper Case Charact
'''
s=input('Enter a string:')
if len(s)%2==1:
    if 'a'<=s[len(s)//2]<='z' or 'A'<=s[len(s)//2]<='Z':
        if 'A'<=s[len(s)//2]<='Z':
            print(s[len(s)//2])
        else:
            print('mid char is not upper case')
    else:
        print('mid char is not an alphabet')
else:
    print('there is no middle char')
'''


##################################

#while loop

#q39. wap to print hello 5 times
'''
s='hello'
i=1
while i<=5:
    print(s)
    i=i+1
'''

#q40. wap to print the even numbers between 1 to n - print n natural numbers
'''
n=int(input("Enter a number:"))
i=1 
while i<=n:
    if i%2==0: 
        print(i)
    i+=1
'''

#q41. wap to print multiplication table of a given program
'''
n=int(input("Enter no. to print the multiplication table of:"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i=i+1
'''

#q42. wap to find the sum of n natural numbers
'''
n=int(input("Enter a number to find n natural numbers:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum of",n,"natural numbers is",sum)
'''

#q43. wap to find the product of n natural numbers/factorial of a number
'''
n=int(input("Enter number to find factorial of number:"))
prod=1
i=1 #or i=2
while i<=n:
    prod=prod*i;
    i=i+1
print("Factorial of",n,"is",prod)
'''

#q44. Wap to print all the characters of a string
'''
print('to print all the characters of a string')
s=input('enter a string:')
i=0
while i<len(s):
    print(s[i])
    i=i+1
'''

#45.Wap to print all the characters present at even index of a string.
'''
print('to print all the characters present at even index of a string.')
s=input('enter  a string:')
i=0
while i<len(s):
    if i%2==0:
        print(s[i])
    i=i+1
'''

#46.Wap to extract all the lowercase characters present in a string.
'''
print('to extract all the lowercase characters present in a string.')
s=input('enter a string:')
i=0
out=''
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=s[i]
    i=i+1
print('string after extracting only lowercase characters:',out)
'''


#q47. wap to extract the vowels present in a string
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

#q48. wap to print the factors of a number
#factors start form 1 and always less than n
'''
n=int(input("Enter a number to find the factors of:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i=i+1
'''

#49.Wap to toggle a string.
'''
print('to toggle a string')
s=input('enter a string to toggle it:')
i=0
out=''
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=chr(ord(s[i])-32)
    elif 'A'<=s[i]<='Z':
        out+=chr(ord(s[i])+32)
    else:
        out+=s[i]
    i+=1
print('toggled string:',out)
'''
#q50. wap to reverse a number
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

#q51. wap to print the sum of all digits of a number
'''
n=int(input("Enter a number to find the sum of digits:"))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print("Sum of digits is:",sum)
'''

#q52. wap to check whether a number is perfect number or not
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

#53.Wap to login to phonepe by entering correct otp.-?
'''
otp='2412'
p=input('enter otp to login to phonepe:')
if p==otp:
    print('logged in successfully')
else:
    print('loign unsuccessful')
'''

#54.Wap to run infinite loop until user enters the correct password
'''
otp='4211'

while otp!=p:
    p=input('Enter otp:')
print('logged in successfully')
'''

#55.Wap to extract all the even integers present in a tuple at odd index.
'''
t=eval(input('Enter a tuple:'))
i=0
l=[]
while i<len(t):
    if t[i]%2==0:
        l.append(t[i])
    i+=1
print(tuple(l))
'''

#56.Wap to remove duplicates from a list without converting into set.
'''
l=eval(input('Enter a list to remove duplicates:'))
out=[]
i=0
while i<len(l):
    if l[i] not in out:
        out.append(l[i])

    i+=1
print(out)
'''

#57.Wap to find the sum of all the odd numbers between the given range
'''
start=int(input('enter start of range:'))
end=int(input('enter end of range:'))
i=start
sum=0
while i<=end:
    if i%2==1:
        sum+=i
    i+=1
print(sum)
'''

#58.Wap to find the greatest number in a given list of integers.
'''
l=eval(input('Enter a list of integers to find the greatest number:'))
greatest=l[0]
i=0
while i<len(l):
    if l[i]>greatest:
        greatest=l[i]
    i+=1
print('greatest is:',greatest)
'''

#59.Wap to find the sum of cube of a number in a string.-? all numbers or only one digit?
'''
s=input('enter  a string containing a number:',)
i=0
sum=0
while i<len(s):
    if '0'<=s[i]<='9':
        sum=sum+int(s[i])**3
    i+=1
print('sum of all numbers in string:',sum)
'''

#q60. wap to check whether the number is armstrong or not
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

#q61. wap to get the following output:
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

#62.Wap to check the given number is prime or not.(while loop)
'''
n=int(input('enter to check for prime:'))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print('it is prime')
else:
    print('it is not prime')
'''

#q63. wap to check if palindrome
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

#64.Wap to find the HCF of two numbers.
'''
a=int(input('enter num 1:'))
b=int(input('enter num 2:'))
i=1
hcf=1
while i<=a//2 and i<=b//2:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1
print('hcf:',hcf)
'''



#q65. wap to convert binary to decimal
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

#q66. wap to convert an int to binary
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

#67.Wap to count the number of words in a string.
'''
s=input('Enter a sentence:')
count=0
i=0
while i<len(s):
    print(s[i],end='')
    if s[i]==' ':
        count+=1
    i+=1
print('count of words:',count+1)
'''

#68.Wap to guess the number.
'''
n=132
print('guess the number')
num=int(input('enter your guess:'))
while num!=n:
    num=int(input('try again:'))
print('correct!')
'''

#69.Wap to find the common elements in two sets -?cos set cant be indexed
'''
s1=eval(input('enter set1:'))
s2=eval(input('enter set2:'))

out=set()
        
while len(s1)!=0:   #OR - while s1:
    val=s1.pop()
    if val in s2:
        out.add(val)
print(out)
'''       

#70.Wap to find the product of all the digits present in a number.
'''
n=int(input('enter a number:'))
prod=1
while n>0:
    d=n%10
    prod=prod*d
    n=n//10
print('product of digits:',prod)
'''


############################

#for loop

#71.Wap to print all the integers present in a list.
'''
l=eval(input('enter a list:'))
for i in l:
    if type(i)==int:
        print(i)
'''

#72.Wap to find the length of homogenous tuple without len()
'''
t=eval(input('enter a tuple:'))
count=0
for i in t:
    count+=1
print('length of tuple:',count)
'''

#73.Wap to extract all the even numbers present in a list.
'''
l=eval(input('enter a list:'))
out=[]
for i in l:
    if type(i)==int:
        if i%2==0:
            out.append(i)
print('even nos in list:',out)
'''        

#74.Wap to remove duplicates from list
'''
l=eval(input('enter a list:'))
out=[]
for i in l:
    if i not in out:
        out.append(i)
print('after removing duplicates:',out)
'''

#75.Wap to reverse a string without using slicing.
'''
s=input('enter a string:')
rev=''
for i in s:
    rev=i+rev
print('reversed string:',rev)
'''
    
#76.wap to extract all the lowercase characters in a string only if the ascii value is even.
'''
s=input('enter a string:')
out=''
for ch in s:
    if 'a'<=ch<='z':
        if ord(ch)%2==0:
            out+=ch
print('lowercase characters with even ascii:',out)
'''

#77.Wap to check whether the last digit of an integer is even or not.-?
'''
n=int(input('enter a number:'))
if (n%10)%2==0:
    print('last digit is even')
else:
    print('last digit is not even')
'''

 #78.Wap to extract all the key value pairs from the dictionary only if the keys are of
 #string datatype and values are integers.
'''
d=eval(input('enter a dictionary:'))
out={}
for k in d:
    if type(k)==str and type(d[k])==int:
        out[k]=d[k]
print('output:',out)
'''

 #79.Wap to extract key value pairs from the dictionary only if both keys and values are exactly same.
'''
d=eval(input('enter a dictionary:'))
out={}
for k in d:
    if k==d[k]:
        out[k]=d[k]
print('result:',out)       
'''

 #80.Wap to get the following output using len function.
 #S=’power star’
 #Out={‘power’:5,’star’:4}
'''
s=input('enter a sentence')
s=s+' '
out={}
word=''
for ch in s:
    if ch!=' ':
        word+=ch
    else:
        out[word]=len(word)
        word=''
print('output:',out)
'''

 #81.Wap to get the following output.
 #S=’power star’
 #Out={‘power’:’rewop’,’star’:’rats’}
'''
s=input('enter a sentence:')
s=s+' '
word=''
out={}
for ch in s:
    if ch!=' ':
        word=word+ch
    else:
        out[word]=word[::-1]
        word=''
print('output:',out)
'''

#82. wap to extract all the non default values from a list.
'''
l=eval(input('enter a list:'))
out=[]
for i in l:
    if bool(i)==True:
        out.append(i)
print('non default values of the list are:',out)
'''

 #83.Wap to check whether the list is homogenous or not.-?
'''
l=eval(input('enter a list:'))
item1=l[0]
count=0
for item in l:
    if type(item)==type(item1):
        count+=1
if count==len(l):
    print('List is homogeneous')
else:
    print('List is heterogeneos')
'''      


 #84.Wap to replace the space by * present in a string
'''
s=input('enter:')
out=''
for ch in s:
    if ch==' ':
        out+='*'
    else:
        out+=ch
print('result:',out)
'''

 #85.Wap to count the number of occurrence of a specified character.

'''
s=input('enter a string:')
ch=input('enter character to find its frequency:')
count=0
for c in s:
    if c==ch:
        count+=1
print(f'Frequncy of {ch} in {s} is {count}')
'''


#86. Wap to get the following output.
# S=’always keep smiling’
 #Out-‘syawla peek gnilims’
'''
s=input('enter a sentence:')
s=s+' '
word=''
out=''
for ch in s:
    if ch!=' ':
        word=ch+word
    else:
        out=out+word+ch
        word=''
print('result:',out)
'''

 #87. Wap to get the following output.
 #In=’push maadi kushi padi’
 #Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’}
'''
s=input('enter a sentence:')
d={}
s=s+' '
word=''
for ch in s:
    if ch!=' ':
        word=word+ch
    else:
        if len(word)%2==0:
            d[word]=word[0]+word[-1]
        else:
            d[word]=word[len(word)//2]
        word=''
print('result:',d)
'''

#88.Wap to toggle a string.
'''
print('to toggle a string')
s=input('enter a string to toggle it:')

out=''
for i in s:
    if 'a'<=i<='z':
        out+=chr(ord(i)-32)
    elif 'A'<=i<='Z':
        out+=chr(ord(i)+32)
    else:
        out+=i
    
print('toggled string:',out)
'''



# 89.Wap extract upper, lower, digit and special characters present in a string to different. output variable
#q8.Wap extract upper, lower, digit and special characters present in a string to different. output variable
'''
s=input('enter a string:')
upper=''
lower=''
digit=''
special=''

for ch in s:
    if 'a'<=ch<='z':
        lower+=ch
    elif 'A'<=ch<='Z':
        upper+=ch
    elif '0'<=ch<='9':
        digit+=ch
    else:
        special+=ch
print('upper:',upper)
print('lower:',lower)
print('digits:',digit)
print('special:',special)
'''

 #90. Wap to get the following output.
 #S=’hai hello ‘
 #Out={‘hai’:’ai’,’hello:’eo’}
'''
s=input('enter a string:')
word=''
d={}
vowel=''
for ch in s:
    if ch!=' ':
        word+=ch
    else:
        for c in word:
            if c in 'aeiouAEIOU':
                vowel+=c
        d[word]=vowel
        word=''
        vowel=''
print(d)
        
'''
 #91. Wap to get the following output.
 #S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org’]
 #Out=[‘com’,’py’,’html’,’org’]
'''
s=input('enter a list of domain name:')
for dn in s:
    i=0
    while i<len(s):
        if dn=='.':
'''


 #92. Wap to get the following output.
 #S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
 #Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],’org’:[‘www’]}
