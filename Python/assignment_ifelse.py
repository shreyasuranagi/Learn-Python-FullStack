'''
#q1. wap to check whether char is uppercase alphabet or not
ch=input("enter a single character:")
if ch>='a' and ch<='z': # if 'a'<=ch<='z': => should be for upper case
    print("it is not upper case") #cant say it is lower
else:
    print("upper")
'''

#######################
'''
#q2. wap to check whether character is digit or not
ch=input("Enter a single character:")
if ch>='0' and ch<='9':
    print(ch,"is a digit")
else:
    print(ch,"is not digit")
'''

##############
'''
ch=input("enter a single ch:")
if ch in '0123456789':
    print("digit")
else:
    print('not a digit')
'''

################
'''
#q3. wap to check whether num is divisble by both 3 and 5
n=int(input("enter a number:"))
if n%3==0 and n%5==0:
    print(f"{n} is divisible by both 3 and 5 and their square is {n*n}")
else:
    print(f"{n} not divisble by both 3 and 5")
'''

'''
#q4. wap to check whether the given string is keyword or not
s=input("enter a string to check:")
import keyword
k=keyword.kwlist
if s in k:
    print(f"{s} is  a keyword")
else:
    print(f"{s} is not a keyword")
'''

#################
'''
ch=input("Enter a character:")
if not('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'):
    print(f"{ch} it is a special character")
else:
    print(f"{ch} it is not a special character")

'''

##################
'''
s=int(input("Enter a string to check palindrome:"))
if s==s[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome {s[::-1]}")
'''

#################
'''
d=eval(input("Enter any data to check mutable: "))
#if type(d)==type([]) or type(d)==type(set()) or type(d)==type({}):
if type(d) in [list,set,dict]:
    print("it is mutable")
else:
    print("it is not mutable")
'''

################
'''
x=eval(input("enter:"))
y=eval(input("enter:"))
#if id(x)==id(y):
if x is y:
    print("pointing to same memory")
else:
    print("not pointing to same memory")

'''
################

l=eval(input("enter:"))
print("length of list:",len(l))
if len(l)%2==1:
    print("there is a single middle value",end="--")
    print("the middle value is:",l[int(len(l)/2)]) #l[len(l)//2]
else:
    print("there is no middle value")

