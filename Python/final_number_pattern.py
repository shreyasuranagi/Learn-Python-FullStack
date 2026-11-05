

#1

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i+j==(r//2+1)+1 or i==r or  j==r//2+1:
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
print()
print('='*30)


#2

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r//2+1 or i==r or(j==c and i<=r//2+1) or (j==1 and i>=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
print()
print('='*30)





print()
print('='*30)
#3

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or j==r or i==r or (i==r//2+1 and j!=1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()


print()
print('='*30)
#4

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==r//2+1 or i+j==(r//2+1)+1 or j==r//2+1:
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()


print()
print('='*30)
#5

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or i==r//2+1 or (j==r and i>=r//2+1) or (j==1 and i<=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()

print()
print('='*30)
#6

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or j==1 or i==r//2+1 or (j==r and i>=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()

print()
print('='*30)
#7

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i+j==r+1:
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()

print()
print('='*30)
#8

r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or j==c or (i==1) or (i==r ) or (i==r//2+1 ):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()

print()
print('='*30)
#9


r=5
#r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==c or i==r or i==1 or i==r//2+1 or (j==1 and i<=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
