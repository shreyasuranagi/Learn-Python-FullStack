#number pattern matrix
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1):
        print(i,j,sep='', end=' ')
    print()

r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1) :
        if (1<=i<r//2 and j==1) or(i==1 and 1<=j<=c//2) or (j==c//2 and 1<=i<=r//2) or (i==r//2 and 1<=j<=c//2) or (j==1 and i==r//2+1) or (i>=r//2+1 and j==1 and i!=c) or (i==r and 2<=j<=c-1) or (j==c and i!=r) or (i==1 and r//2+1+1<=j<=c) or (i==r//2+1 and 2<=j<=r//2+1+1) or (j==r//2+1+1 and i<=r//2+1):
            print('*',sep='',end=' ')
        else:
                print(' ',sep='',end=' ')
    print()



'''
#copy
r=5
r=int(input('Enter rows/cols (odd):'))
c=r
for i in range(1,r+1):
    for j in range(1,c+1) :
        if (1<=i<r//2 and j==1) or(i==1 and 1<=j<=c//2) or (j==c//2 and 1<=i<=r//2) or (i==r//2 and 1<=j<=c//2) or (j==1 and i==r//2+1) or (i>=r//2+1 and j==1 and i!=c) or (i==r and 2<=j<=c-1) or (j==c and i!=r) or (i==1 and r//2+1+1<=j<=c) or (i==r//2+1 and 2<=j<=r//2+1+1) or (j==r//2+1+1 and i<=r//2+1):
            print('*',sep='',end=' ')
        else:
                print(' ',sep='',end=' ')
    print()
'''
