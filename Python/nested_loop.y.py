'''
#nested loops
c=0
for i in range(1,15,3):
    for j in range(2,20,4):
        for k in range(5,50,10):
            print(i+j+k)
            c+=1
print('count=',c)
'''

'''
#wap to flatten a nested list using nested loops

l=[[1,2,3],[4,6],[7,8,9]]
flatten_list=[]
for outer_elem in l:
    for inner_elem in outer_elem:
        flatten_list.append(inner_elem)
print(flatten_list)
'''

'''
#wap to get the following output. without length function. -using nested loop
 #S=’power star’
 #Out={‘power’:5,’star’:4}
s='hello world'
out={}

for w in s.split():
    count=0
    for i in w:
        count+=1
    out[w]=count
print(out)
'''

'''
#put.
 #S=’power star’
 #Out={‘power’:2,’star’:1} (no of vowels is key)

s='power star'
out={}

for w in s.split():
    vow=0
    for i in w:
        if i in 'aeiouAEIOU':
            vow+=1
    out[w]=vow
print(out)
'''

'''
#Q
#s='power star'
#out = { 'power' : ['rewop',2,'pwr'] ...}

s='power star'
out={}
for w in s.split():
    count=0
    for ch in w:
        if ch in 'aeiouAEIOU':
            count+=1

    out[w]=[w[::-1],count,w[::2]]
print(out)
'''
'''
#q120. Wap to get the following output.
 #In=[‘hello’,227,3.4,’last’,189,34]
 #Out=[722,981,43]

l=['hello',227,3.4,'last',189,34]
out=[]
for n in l:
    if type(n)==int:
        #prog to reverse it
        rev=0
        while n>0:
            d=n%10
            rev=rev*10+d
            n=n//10

        out.append(rev)
print(out)



#print using string to reverse -> dont use slicing for integers tho
l=['hello',227,3.4,'last',189,34]
out=[]
for n in l:
    if type(n)==int:
        out.append(int(str(n)[::-1]))
print(out)
'''

'''
#114.the following output.
# S=’kabab is love’
# Out={‘kb’:(‘kbb’,3,’bbk’),’is’:(‘s’,1,’s’),’le’:(‘lv’,2,’vl’)}
# { 1st+last char: (consonant,no of consonant,rev of consonant)}

s='kabab is love'
out={}
for w in s.split():
    con=''
    for ch in w:
        if ch not in 'aeiouAEIOU':
            con=con+ch
    out[w[0]+w[-1]] = (con,len(con),con[::-1])
print(out)
        
'''


#q115. to get the following output.
# In=[100,200,35,40,60]
# Out=[335,235,400,395,375] (total sum-value)

''' !wrong way cos s is local variable cant be accessed outside of loop
inp=[100,200,35,40,60]
out=[]
s=0
for i in inp:
    if s!=0:
        for j in inp:
            s=s+j
    out.append(s-i)
print(out)

'''
'''
#correct
inp=[100,200,35,40,60]
out=[]
for i in inp:
    s=0
    for j in inp:
        s=s+j
    out.append(s-i)
print(out)
'''


#q116. Wap to get the following output. ?
# In=’bacbcaabbaa’
# Out=’b4a5c2'
'''
inp='bacbcaabbaa'
out=''
for ch in inp:
    count=0
    if ch not in out:
        for char in inp:
            if char==ch:
                count+=1
        out=out+ch+str(count)
print(out)
'''

#q118.Wap to check whether the number is strong or not.
#A Strong Number is a special number where the sum of the factorials of its digits
#is equal to the number itself.

num=int(input('Enter:'))
n=num
s=0
#loop to get digits
while num>0:
    d=num%10
    #loop to get factorial of each digit
    i=1
    prod=1
    while i<=d:
        prod=prod*i
        i=i+1
    s=s+prod
    num=num//10

if n==s:
    print(n,'is a strong number')
else:
    print(n,'is not a strong number')


#119.Wap to get the following output.
 #In={10:’star’,20:’bye’,30:’moon’,40:’apple’}
 #Out={10:’a’,20:’e’,30:’oo’,40:’ae’}

#1. traverse thru dict
    #2. traverse thru each value for vowel
'''
d={10:'star',20:'bye',30:'moon',40:'apple'}
out={}
for k in d:
    out[k]=''
    for ch in d[k]:
        if ch in 'aeiouAEIOU':
            out[k]=out[k]+ch
print(out)
'''

#120. Wap to get the following output.
 #In=[‘hello’,227,3.4,’last’,189,34]
 #Out=[722,981,43]




