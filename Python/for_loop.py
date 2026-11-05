#q1 wap to extract all the int present in a list
'''
l=eval(input('enter a list to extract int from:'))
out_list=[]
for item in l:
    
    if type(item)==int:
        out_list.append(item)

print(out_list)
'''

#q2 wap to reverse string without using slicing
'''
s=input("Enter a string to reverse:")
rev_str=''
for ch in s:
    rev_str=ch+rev_str
print("Reversed string is:",rev_str)

'''

#q3 wap to remove duplicates from a list
'''
[1,3,2,4,1,3]
[2,4]
out=[]
l=eval(input('Enter:'))
for n in l:
    if n not in out:
        out.append(n)
print(out)
'''

#q3 wap to convert upper to lower and lower to upper
'''
s=input("Enter a string to switch cases of characters:")
out=''g
for ch in s:
    if 'a'<=ch<='z':
        ch=chr(ord(ch)-32)
'''

#q4 wap to extract the even integer present at odd index of a list
'''
l=eval(input('Enter:'))
out=[]
for i in range(0,len(l),1):
    if i%2==1:
        if type(l[i])==int:
            if l[i]%2==0:
                out.append(l[i])
print(out)
'''

#q5 wap to convert string to dictionary of its index:character
#way to get the following output.
# S=’hai hello ‘
# Out={‘hai’:’ai’,’hello:’eo’}

'''
s=input('enter:')
d={}
for i in range(len(s)):
    d[i]=s[i]
print(d)
'''

#q6. wap to get the following output-
#Wap to get the following output.
#L=[‘hai’,34,3.4,’hello’,90,’byebye’]
#Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’}
'''
l=eval(input('Enter a list:'))
d={}
for item in l:
    if type(item)==str:
        d[item]=item[0]+item[-1]
print(d)
'''

#q7. wap to count the no of occurrences(frequency) of a specific character.
'''
s=input('enter a string:')
ch=input('enter character to find its frequency:')
count=0
for c in s:
    if c==ch:
        count+=1
print(f'Frequncy of {ch} in {s} is {count}')
'''

#q8.Wap extract upper, lower, digit and special characters present in a string to different. output variable
'''
s=input('enter a string:')
upper=''
lower=''
digit=''
special=''

for ch in s:
    if 'a'<=ch<='z':
        lower+=ch
    elif 'A'<=ch<='Z':
        upper+=ch
    elif '0'<=ch<='9':
        digit+=ch
    else:
        special+=ch
print('upper:',upper)
print('lower:',lower)
print('digits:',digit)
print('special:',special)
'''

#q. wap to find length of a collection without using len() function
'''
col=eval(input('Enter any collection:'))
count=0
for item in col:
    count+=1
print('length of collection:',count)
'''

#q78. 
#extract key val pairs if key is string and val is int
'''
d=eval(input('enter a dictionary:'))
out={}
for k in d:
    if type(k)==str:
        if type(d[k])==int:
            out[k]=d[k]
print('result:',out)
'''

#q80
'''
s=input('enter a sentence:')
word=''
outd={}
l=0
for ch in s:
    if ch!=' ':
        word=word+ch
        l+=1
    else:
        outd[word]=len(word)
        word=''
        l=0
outd[word]=l
print(outd)
'''

#q86. wap to reverse each word in a sentence
'''
s=input('Enter :')
out=''
word=''

for ch in s:
    if ch!=' ':
        word=word+ch  #OR word=i+word
    else:
        out=out+word[::-1]+' '  #then- out=out+word+' '
        word=''
out=out+word[::-1]
print(out)
'''
'''
#OR - using split()
s=input('enter a sentence:')
out=''
#l=s.split()
for word in s.split():
    out+=word[::-1]
    out+=' '
#print(out)
print(out.strip())
'''
'''
#OR - using join
s=input('Enter a sentence:')
out=[]
for i in s.split():
    out.append(i[::-1])
print(' '.join(out))
'''
#assign
'''
#q91. wap to split the domain names from  a list of domain names
l=['jiocinema.com','file.py','web.html','amazon.com','www.org']
out=[]
for dn in l:
    split_dn=dn.split('.')
    #print(split_dn)
    if split_dn[1] not in out:
        out.append(split_dn[1])
print(out)
'''

'''
#to remove duplicates-
final=[]
for item in out:
    if item not in final:
        final.append(item)
print(final)
'''
#assignment
'''
#q87. Wap to get the following output.
 #In=’push maadi kushi padi’
 #Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’}

s=input('Enter a sentence:')
d={}
l=s.split()
for w in l:
    if len(w)%2==0:
        d[w]=w[0]+w[-1]
    else:
        d[w]=w[len(w)//2]
print(d)
'''

#92. wap to get the following output.
# S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
# Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],
# ’org’:[‘www’]}
'''
l=eval(input('Enter a list:'))
out={}
extl=[]
for item in l:
    if item.split('.')[1] not in extl:
        extl.append(item.split('.')[1])

for item in l:
    extn=item.split('.')[1]
    if extn in extl:
        if extn not in out:
            out[extn]=[]
            out[extn].append(item.split('.')[0])
        else:
            out[extn].append(item.split('.')[0])
print(out)
'''

#100.Wap to find the longest word in a string.
'''
s=input('enter a sentence to find the longest word:')
lw=''
for word in s.split():
    if len(word)>len(lw): #gives first longest word. consider first occurence
        lw=word
print('longest word:',lw,'with length:',len(lw))
'''

#105. Wap to get the following output.
 #In=’10100011231’
# Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)

#inp='10100011231'
'''
inp=input('enter:')
out=''
for c in inp:
    if c=='0':
        out+='1'
    if c=='1': #or use elif- better because here, both if are checked
        out+='0'
print('output:',out)
'''

#92. wap to get the following output.
# S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
# Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],
# ’org’:[‘www’]}
'''
l=eval(input('Enter:'))
res={}
for i in l:
    s=i.split('.')
    if s[1] not in res:
        res[[s[1]]=s[0]
    else:
        res[s[1]].append(s[0])
print(res)
'''

#q. wap to find the greatest integer in a list of integers
'''
l=eval(input('Enter a list of integers:'))
greatest=0
for i in l:
    if i>greatest:
        greatest=i
print('Greatest integer:',greatest)
'''

#q. wap to find the second greatest integer in a list of integers
'''
l=eval(input('Enter a list of integers:'))
greatest=0
second=0
for i in l:
    if i>greatest:
        second=greatest
        greatest=i
        
print('Second greatest:',second)
'''

''''
numbers=eval(input('Enter a list of integers:'))
greatest=0
second=0
for num in numbers:
    if num>greatest:
        second=greatest
        greatest=num
    elif num>second and num!=greatest:
        second=num
'''

##1,2,42,4
numbers=eval(input('Enter a list of integers:'))
greatest=0
second=0
for num in numbers:
    if num>greatest:
        second=greatest
        greatest=num
    elif num>second:
        second=num
print(greatest,second)



'''
#08.Wap to get the following output.
# In=’127342’
# Out=’242173’ (extract even and odd digits separately and concatenate both)

inp=input('Enter:')
odd=''
even=''
for i in inp:
    if int(i)%2==0:
        even+=i
    else:
        odd+=i
print('result:',even+odd)
'''

'''
#106.Wap to get the following output.
 #In=’abacbaacc’
 #Out={‘a’:4,’b’:2,’c’:3}

s=input('Enter:')
out={}
for c in s:
    if c not in out:
        out[c]=1
    else:
        out[c]+=1
print(out)
'''
'''
#OR
#usint count and full iteration
s=input('Enter:')
out={}
for c in s: #repeats len(s) no. of times
    out[c]=s.count(c)
print(out)
'''
'''

#OR-more efficient
s=input('Enter:')
out={}
for c in set(s):
    out[c]=s.count(c)
print(out)

'''
