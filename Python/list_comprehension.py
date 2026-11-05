#list comprehension

#syntax 1
'''
l=[i for i in range(1,11)] 
print(l)

#print even nos from 1 to 10
even=[ num  for num in range(1,11) if num%2==0] #here its working as filter??
print(even)

#print square if even , cube if odd between 1 to 10

#i need all nums 1 to 10
# i ahve  a condition if else
# i cna weite in single line

even=[num**2 if num%2==0 else num**3 for num in range(1,11)]
print(even)


#wap to extrace only the str which starts with a
l=['a','hi','Ab','bye','apple']

#out=[ w for w in l if w.startswith('a') ]

#try with filter
out= list(filter( lambda n: n[0]=='a', l))
print(out)

#wap to replace negative numbser with 0 (others reamin the same)
l=[1,-3,2,-5,2,3,-1]
print(l)
neg_replace= [ 0 if num<0 else num  for num in eval(input())]
print(neg_replace)


#wap to create list that contains len of words present in the input list
l=['a','hi','ab','bye','apple']

len_word=[ len(w) for w in l ]
print(len_word)




l1=[1,2]
l2=[3,4]
#out=[1,2,3,4]

out=[ (i,j) for i in l1 for j in l2]
print(out)
out=[ print(i,j) for i in l1 for j in l1] #makesense to use this? or map?
print(out)

#out = [4,5,5,6]
out=[ i+j for i in l2 for j in l1]
print(out)





#set comprehension

s='donkeyd'
#out = { (0,'d'),(1,'o')..}
out = { (i,s[i]) for i in range(0,len(s)) }
print(out)

out = { (s.index(i,s.index(i)),i) for i in s}
print(out)
'''

#enumerate function
'''
#to get btoh index and value

print(enumerate('abcd'))
#enumerate object

print( (i,j) for i,j in enumerate('abcd'))

print({ (i,j) for i,j in enumerate('abcd')})

for i,j in enumerate('abcd'):
    print(i,j)

'''

#zip
'''
l1=[1,2,3.5,6,7,8]
l2=[10,21,11,14]

for i in zip(l1,l2):
    print(i)

for i,j in zip(l1,l2):
    if type(i)==int:
        print(i,j)

#q
l=['apple','heaven','world','army','animal','air','pink']
d={ w:len(w) for w in l}

print(d)

s='heaven'
d={ i:ord(i) for i in s if ord(i)%2==0 }
print(d)


print({chr(i):i for i in range(97,123)})

l=[1,2,3]
l2=[4,5,6]
d={ i:j for i,j in zip(l,l2) }
print(d)


l1=[1,2,[1,2,3],'hii']
l2=[2,[1,2],3.5,1]
print(l1)
print(l2)
print({ i:j for i,j in zip(l1,l2) if type(i) not in [list,set,dict] })
'''

l=['hii','dad','mom','pink','cherry']
#out - {'hii': 'iih', 'dad': 3, 'mom': 3, 'pink': 'knip', 'cherry': 'yrrehc'}

print({ w:len(w) if w==w[::-1] else w[::-1]  for w in l})





