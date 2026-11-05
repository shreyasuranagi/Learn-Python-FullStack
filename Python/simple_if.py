'''
#q1. check whether a number is positive
age =int(input('Enter your age'))
if age>=18:
    print(age>=18,end='-')
    print("you are eligible to vote, your age is",age)
'''

'''
#q2. check whether a number is positive
num=eval(input("enter a number to check positive or not:"))
if num>=0:
    print(num,' is positive')
'''

#q3. wap to print whether square of an int number is es even or not
##num=int(input("enter an int number:"))
##sqnum=num*num
##if sqnum%2==0:
##    print("square of",num," is",sqnum,"It is even")

'''
q3. wap to print square of a int number if it is even
num=int(input("enter:"))
if num%2==0:
    print(num,"is even and its square is",num**2)
'''

'''
#q4. wap to check whether char is vowel or not

cin=input('Enter a single character')
if cin=='a' or cin=='e' or cin=='i'or cin=='o' or cin=='u' or cin=='A' or cin=='E' or cin=='I' or cin=='O' or cin=='U':
    print("It is  a vowel")


cin=input('Enter a single character:')
if cin in 'aeiouAEIOU':
    print(cin,"is a vowel")
'''

#wap to print the square of a number if it is even , else print the cube of it
n=float(input("Enter:"))
if n%2==0:
    print("Square of",n,"is",n*n)
else:
    print("Cube of",n,' is',n**3)


