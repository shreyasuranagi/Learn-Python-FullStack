#while -> recursion



#q39.Wap to print python for 5 time
'''
def print5(i=0):
    if i==5:
        return
    print('python')
    return print5(i=i+1)

print5()
'''

#OR to print a string n times
def print5(n,s,i=0):
    if i==n:
        return
    print('python')
    return print5(n,s,i=i+1)
s=input('Enter string to be repeated:')
n=input('Enter number of times to repeat:')
print(n,s)


#40.Wap to print n natural numbers.
#using while
n=int(input('Enter n:'))
i=1
while(i<=n):
    print(i)

    i=i+1

#recursion



    
