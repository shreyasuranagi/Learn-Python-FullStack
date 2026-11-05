#wap to find the factorial of a number / product of n natural numbers
# 5!=1*2*3*4*5
'''
n=int(input('Enter a  number to find its factorial'))
i=1
prod=1
while i<=n:
    prod = prod * i
    i=i+1
print('Factorial: ',prod)
'''
#recursion

def factorial(n, i=1, prod=1):
    if i==n:
        print(f' factorial({n},{i},{prod}')
        return prod*i
    print(f' factorial({n},{i},{prod}')
    return factorial(n, i=i+1, prod=prod*i)

n=int(input('Enter a  number to find its factorial'))
print(factorial(n))


