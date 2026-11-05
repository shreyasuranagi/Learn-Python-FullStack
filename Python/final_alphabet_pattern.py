
print()
print('='*60)
print()
#A -slanted

c=9
r=5
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        
        #if i+j==6 or j-i==4 or ( i==3 and 4<=j<=6):
        if i+j==r+1 or j-i==r-1 or (i==r//2+1 and r-1<=j<=r+1): 
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print('='*60)
print()


#block A
c=9
r=5
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        
        if (i==1 and (j!=1 and j!=c)) or (j==1 and i!=1) or (j==c and i!=1) or i==r//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#B

c=4
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        
        if j==1 or (i==1 and j!=c) or (i==r and j!=c) or i==r//2+1 or (j==c and i!=1 and i!=r):
        
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#C
c=4
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        
        if (i==1 and j!=1) or (i==r and j!=1) or (2<=i<=r-1 and j==1):
            
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()
print()
print('='*60)
print()

#D
c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        
        #if j==1 or (j!=c and (i==1  or j==c))  :
        if (i==1 and j!=c) or (j==c and i!=1 and i!=r) or (i==r and j!=c) or j==1:
            
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#E
c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or i==1 or i==r or i==r//2+1:
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#F
c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or i==1 or i==r//2+1:
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#G
c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if (j==1 and i!=1 and i!=r) or (i==1 and j!=1) or (i==r and j!=1) or (j==c and r//2+1<=i<=r-1 ) or (i==r//2+1 and j==c-1):
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#H
c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or j==c or i==r//2+1:
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#I
c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or j==c//2+1:
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#J

c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or (j<=r//2 and i==r) or j==c//2+1:
            print('*',end=' ')
        
        else:
            print(' ',end=' ')
    print()

print()
print('='*60)
print()

#K
c=7
r=8
c=5
r=7
#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or i+j==6 or i-j==2:
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#L
c=7
r=8

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or i==r:
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#M
c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or j==5 or (i==j and i<=r//2) or (i+j==c+1 and i<=r//2):
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#N
c=5
r=5

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or j==c or i==j:
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#O
c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if  (j==1 and i!=1 and i!=r) or (i==1 and j!=1 and j!=c) or (j==c and i!=1 and i!=r) or (i==r and j!=1 and j!=c):
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()
print()
print('='*60)
print()




#P

c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or (i==1 and j!=c) or (i==r//2+1 and j!=c) or (j==c and i<r//2+1 and i!=1) :
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#Q
c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if  (j==1 and i!=1 and i!=r) or (i==1 and j!=1 and j!=c) or (j==c and i!=1 and i!=r) or (i==r and j!=1 and j!=c) or (i-j==2 and i>r//2+1):
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#R
c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or (i==1 and j!=c) or (i==r//2+1 and j!=c) or (i-j==2) or (j==c and i<r//2+1 and i!=1) :
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#S
c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if (i==1 and j!=1) or (i==r and j!=c) or (i==r//2+1) or (j==1 and i!=1 and i<=r//2) or (j==c and i>=r//2+1 and i!=r):
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()
print()
print('='*60)
print()

#T

c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or j==c//2+1:
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

#U
c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if (j==1 and i!=r) or (j==c and i!=r) or (i==r and j!=1 and j!=c):
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()
print()
print('='*60)
print()

#V

c=9
r=5

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==j or i+j==c+1:
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()
print()
print('='*60)
print()

#W

c=5
r=7

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j==1 or j==c or (i+j==r+1 and i>r//2+1) or (i-j==2 and i>r//2+1):
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()
print()
print('='*60)
print()

#X

c=5
r=5

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==j or i+j==c+1:
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()
#Y

c=5
r=5

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if ((i==j or i+j==c+1) and i<=r//2+1) or (j==c//2+1 and i>=r//2+1):
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()
print()
print('='*60)
print()

#Z

c=5
r=5

#r=int(input("Enter rows:"))
#c=int(input("Enter columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or i+j==c+1:
            print('*',end=' ')
        
        else:
           print(' ',end=' ')
    print()

print()
print('='*60)
print()

    
