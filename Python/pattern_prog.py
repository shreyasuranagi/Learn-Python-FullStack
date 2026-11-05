#print square matrix
'''
* * *
* * *
* * *
'''
'''
for i in range(1,4):
    for j in range(1,4):
        print('*', end=' ')
    print()
    
'''

######
#primary traingle
'''
*         
  *       
    *     
      *   
        * 
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
########

#lower traingle
'''
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print('*', end=' ' )
        else:
            print(' ',end=' ')
    print()
'''
##########
#upper triangle
'''
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*', end=' ' )
        else:
            print(' ',end=' ')
    print()
'''

##############

#secondary diagonal
'''
n=int(input('Enter a no.:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

############

#lower traingle of secondary diagonal
'''
n=int(input('Enter a no.:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''


#upper triangle of secondary diagonal
'''
n=int(input('Enter a no.:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()
'''

# lower triangle

'''
1         
1 2       
1 2 3     
1 2 3 4   
1 2 3 4 5
'''

'''
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
'''

# upper triangle number
'''
1 1 1 1 1 
  2 2 2 2 
    3 3 3 
      4 4 
        5
'''

'''
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()
'''

# lower triangle alphabet pattern
'''
n=int(input('Enter:'))

for i in range(1,n+1):
    ch=ord('A')
    for j in range(1,n+1):
        if i>=j:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()
'''

# border pattern
'''
* * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
* * * * * * * * *
'''
'''
n=int(input('enter:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')

        else:
            print(' ',end=' ')
    print()
'''
# 2 borders
'''
* * * * * * * 
* : : : : : * 
* :       : * 
* :       : * 
* :       : * 
* : : : : : * 
* * * * * * *
'''
'''
n=int(input('enter:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')

        elif i==2 or i==n-1 or j==2 or j==n-1:
            print(':',end=' ')

        else:
            print(' ',end=' ')
    print()
'''

#border and middle column (odd values only)
'''
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * *
'''
'''
n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        
        if (i==1 or i==n or j==1 or j==n or i==n//2+1 or j==n//2+1):
            print('*', end=' ')
        
        else:
            print(' ',end=' ')
    print()
'''

#border and the center (odd values only)
'''
* * * * * 
*       * 
*   *   * 
*       * 
* * * * *
'''
'''
n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        
        if (i==j and i==n//2+1) or (i==1 or i==n or j==1 or j==n):
            print('*', end=' ')
        
        else:
            print(' ',end=' ')
    print()
'''


#border and cross
'''

n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1:
            print('*', end=' ')
        
        else:
            print(' ',end=' ')
    print()
'''


#assignment


#primary and secondary diagonal
'''
n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(i,j,end=' ')
        else:
            print('  ',end=' ')
    print()
#try odd and even value of n
n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#number pattern
'''
n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1, n+1):
        if j%2==0 and i>=j:
            print(j*j,end=' ')
        elif j%2==1 and i>=j:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
'''
# lower pyramid
'''
n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1,n*2-1+1):
        if i==n or (j-i)==(n-1) or i+j==n+1 :
            print(i,j,sep='',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=int(input('Enter:'))
for i in range(1,n+1):
    for j in range(1,n*2+1-1):
        if i==n or (j-i)==(n-1) or i+j==n+1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''

#OR
'''
n=int(input('Enter:'))
for i in range(5,2*n-1+1):
    for j in range(1,n*2-1+1):
        if i+j==n-1 or i==j or i==2*n-1:
            print(i,j,end=' ')
        else:
            print('  ',end=' ')
    print()

n=int(input('Enter:'))
for i in range(5,2*n-1+1):
    for j in range(1,n*2-1+1):
        if i+j==2*n-1-1 or i==j or i==2*n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#q. upper pyramid

'''
Enter a number:5
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''


'''
#using 2 loops
n=int(input('Enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print('* ',end='')
        else:
            print(' ',end='')
    print()


'''

#using 1 loop

'''
n=int(input('Enter a number:'))

for i in range(1,n+1):
    print(' '*(n-i) + '* '*i)
'''

'''
#using 3 loops
n=int(input('Enter a number:'))
for i in range(1,n+1): #to generate the rows
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print('*',end=' ')
    print()
'''

#diamond pattern
'''
n=int(input('Enter a number:'))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print('* ',end='')
    print()
for i in range(1,n):
    for j in range(i):
        print(' ',end='')
    for k in range(n-i):
        print('* ',end='')
    print()
'''

#OR
'''
n=int(input('Enter a number:'))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)
for j in range(1,n):
    print(' '*j+'* '*(n-j))
'''

#diamond border
'''
n=int(input('Enter a number:'))
print("Here's your Kaju Burfi!")
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        if k==0 or k==i-1:
            print('* ',end='')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n):
    for j in range(i):
        print(' ',end='')
    for k in range(n-i):
        if k==0 or k==n-i-1:
            print('* ',end='')
        else:
            print(' ',end=' ')
    print()
'''

# 4 pieces of diamond

'''
#seconary lower diagonal
for i in range(1,6):
    for j in range(1,6):
        if i+j>=5+1:
            print(j,end=' ' )
        else:
            print(' ',end=' ')
    print()


for i in range(1,6):
    for j in range(1, 6):
        if i>=j:
            print(i,end=' ')
    print()


for i in range(1,6):
    c1=ord('A')
    for j in range(1,6):
        if i<=j:            
            print(chr(c1),end=' ')
            c1+=1
        else:
            print(' ',end=' ')
    print()


for i in range(1,6):
    ch2=ord('A')+i-1
    for j in range(1,6):
        if i+j<=5+1:
            print(chr(ch2),end=' ')
            ch2+=1
        else:
            print(' ',end=' ')
    print()
'''

#############    
#integration
#############
'''   
print()
#upper square

#seconary lower diagonal
for i in range(1,6):
    for j in range(1,6):
        if i+j>=5+1:
            print(j,end=' ' )
        else:
            print(' ',end=' ')
    #print()
#for i in range(1,6):
    for j in range(1, 6):
        if i>=j:
            print(i,end=' ')
    print()


for i in range(1,6):
    c1=ord('A')
    for j in range(1,6):
        if i<=j:            
            print(chr(c1),end=' ')
            c1+=1
        else:
            print(' ',end=' ')
#    print()
#for i in range(1,6):
    ch2=ord('A')+i-1
    for j in range(1,6):
        if i+j<=5+1:
            print(chr(ch2),end=' ')
            ch2+=1
        else:
            print(' ',end=' ')
    print()

'''


###############






