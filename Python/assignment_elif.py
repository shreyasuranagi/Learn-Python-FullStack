#wap to check whether single double or triple digit or more than that
'''
num=abs(int(input("Enter a number:")))
if 0<=num<=9:
    print(num,'is single digit')
elif 10<=num<=99:
    print(num,'is double digit')
elif 100<=num<=999:
    print(num,'is triple digit')
else:
    print(num,'is more than three digits')
'''

###############
#q. wap to check whether number is single or double or triple digit
'''
num=int(input("enter a number:"))
num=str(num)
if len(num)==1:
    print(num,"is a single digit")
elif len(num)==2:
    print("2 digit")
elif len(num)==3:
    print("3 digit")
else:
    print("more than 3 digit")
'''
'''
##--wrong method below--
num=(input("Enter a number:"))
if '0'<=num<='9': #it compares the ascii values
    print(num,'is single digit')
elif '10'<=num<='99':
    print(num,'is double digit')
elif '100'<=num<='999':
    print(num,'is triple digit')
else:
    print(num,'is more than three digits')
'''

#######################
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

########################
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

##########################
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

##############
ch=input("Enter a single character:")
if ord('a')<=ord(ch)<=ord('z'):
    print("upper case  Result:",chr(ord(ch)-32))
elif ord('A')<=ord(ch)<=ord('Z'):
    print("lower case - Result:",chr(ord(ch)+32))
elif ord('0')<=ord(ch)<=ord('9'):
    print('digit -square - Result:',int(ch)**2)
else:
    print('special character-Result:',ch*5)
    


