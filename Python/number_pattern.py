#number pattern matrix
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        print(i,j,sep='', end=' ')
    print()

#1
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i+j==(r//2+1)+1 or i==r or  j==r//2+1:
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''


#2
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r//2+1 or i==r or(j==c and i<=r//2+1) or (j==1 and i>=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''    

#3
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or j==r or i==r or (i==r//2+1 and j!=1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()

'''

#4
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==r//2+1 or i+j==(r//2+1)+1 or j==r//2+1:
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''


#5
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or i==r//2+1 or (j==r and i>=r//2+1) or (j==1 and i<=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''

#6
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or j==1 or i==r//2+1 or (j==r and i>=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''


#7
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i+j==r+1:
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''

#8
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==2 or j==c-1 or (i==1 and 2<=j<=c-1) or (i==r and 2<=j<=c-1) or (i==r//2+1 and 2<=j<=c-1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''

#9
'''
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==c or i==r or i==1 or i==r//2+1 or (j==1 and i<=r//2+1):
            print('*',sep='', end=' ')
        else:
            print(' ',sep='',end=' ')
    print()
'''
