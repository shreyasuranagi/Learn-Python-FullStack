'''
#prime no
n=int(input('enter:'))
c=0
for i in range(2,n):
    c+=1
    if n%i==0:
        print('not prime')
        print('iterations:',c)
        break
else:
    print('prime')
    print('iterations:',c)


#more efficient
n=int(input('enter:'))
c=0
for i in range(2,int(n**0.5)+1):
    c+=1
    if n%i==0:
        print('not prime')
        print('iterations:',c)
        break
else:
    print('prime')
    print('iterations:',c)
'''

#wap to find the first non-repeating char of a string
'''
s=input('enter a string to find the 1st non repeating char of a string:')
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break
else:
    print('there is no non-repeating character')
'''
    
'''
#without count
s=input('enter a string to find the 1st non repeating char of a string:')
count=0
for ch in s:
    if ch in s:
        count
            
'''
#interview
'''

#wap to check whether the str contains only lowercase or not
s=input('Enter:')
for ch in s:
    if not('a'<=ch<='z'):
        print('string contains OTHER than only lowercase chars')
        break  #no need to continue further itertions/chars
else:
    print('string contains ONLY lower case')
'''

'''
#wap to check whether the tuple is homogeneous or not
t=eval(input('Enter a tuple'))
for i in t:
    if type(t[0])!=type(i):
        print('it is not homogeneous')
        break
else:
    print('it is homogeneous')
'''
#or more efficient
'''
t=eval(input('Enter a tuple'))
a=t[0]
for i in t[1:]:
    if type(i)!=a:
        print('it is not homogeneous')
        break
else:
    print('it is homogeneous')
'''

'''
#wap to find the first repeated char
s=input('enter a string:')
for ch in s:
    if s.count(ch)>1:
        print(ch)
        break
else:
    print('there is no repeated char')

'''
'''

#wap to accept valid login and password
import time
uname='shreya'
password='shreya123'
count=0
while True:
    user=input('Enter username:')
    pwd=input('Enter password:')
    count+=1
    if user==uname and pwd==password:
        print('login successful')
        break

    else:
        if count==5:
            print('wait 10s and try again')
            time.sleep(10)
            count=0
        else:
            print('invalid credentials')
            print('please enter valid credentials')


'''
'''
#wap to guess a number with hints
import random
import time
n=random.randint(100,200)
count=0
while True:
    g=int(input('Enter your guess between 100 and 200:'))
    count+=1
    if count==5:
        print('penalty:wait')
        time.sleep(5)
    if g==n:
        print('Correct guess')
        break
    if g>n:
        print('Hint: the number is lesser than',g)
    if g<n:
        print('Hint: the number is greater than',g)
''' 



