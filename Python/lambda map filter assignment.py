#simple if
'''
#q1. Wap to print the square of a number only if it is even.

even = lambda n: n**2 if n%2==0 else None
print(even(3))

#2. Wap to check whether the character is vowel or not.

vowel = lambda ch : ch in 'aeiouAEIOU'
print(vowel('p'))


#q3. Wap to print Ascii value of a character only if it is upper case.
asci = lambda x : ord(x) if 65<=ord(x)<=90 else x
print(asci('c'))
print(asci('C'))

#q 4. Wap to print the cube of a number only if it is divisible by 9 or 6
cube = lambda n: n**3 if n%9==0 or n%6==0 else None
print(cube(12))
print(cube(3))
print(cube(2))

#q 5. Wap to check whether the given integer is 3 Digit number.
dig3 = lambda n: len(str(n))==3
print(dig3(123))
print(dig3(2))
'''



#if else
'''
#q1.Wap to check whether the data is mutable or not.
mutable = lambda data: type(data) in [list,set,dict]
print(mutable(5))
print(mutable([1,2]))


#q2. 18.Consider a tuple of length 2 and check whether the tuple is homogenous or not.
homo = lambda t: type(t[0])==type(t[1])
print(homo((1.3,2.0)))
print(homo(('',2)))


#13.Wap to check whether the given character is special or not.

special = lambda ch: not(65<=ord(ch)<=90 or 97<=ord(ch)<=122 or 48<=ord(ch)<=57)
print(special('t'))
print(special('!'))
'''


#elif
'''
#26.Wap to check the relation between two integer numbers.
rel = lambda a,b: 1 if a==b elif a>b 
print(rel(1,2))
'''


#62.62.Wap to check the given number is prime or not.

isprime = lambda n: len(list((filter(lambda i:n%i==0, range(1,int(n**0.5)+1)))))==2
print(isprime(5))


# 60.Wap to check whether the number is Armstrong or not.
#sum of a list
#print(list(map(lambda i,s=0: s=s+i, [1,2,3])))


