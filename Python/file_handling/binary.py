#binary image
'''
f=open('capture.jpg', 'rb')
data=f.read()
#print(data)
f.close()

f1=open('copyimage.jpg','wb')
f1.write(data)
f1.close()
'''


#binary strings

'''
import pickle
s0= 'everyone' #normal string
s1= b'hello' #hello
s2= 'bye'  #bye
s3=s1.encode()   #hello -> encode

data=[1,2,3,5,6] # list type

c=pickle.dumps(data)
f=open('binary1.txt','rb')
c=f.read()
print(c)
'''



#pickle
'''
import pickle
s0='everyone'
s1=b'hello'
s2='bye'
s3=s0.encode()
s4='normal string'
f=open('binary2.txt','wb')
f.write(s1)
#f.write(s2) # TypeError: a bytes-like object is required, not 'str'
f.write(s3)
#f.write(s4)
f.close()

f=open('binary2.txt','rb')
print('reading via rb mode:')
print(f.read())
f.close()


f=open('binary2.txt','rb')
print('reading via r mode:')
print(f.read())
f.close()

##output-
##reading via rb mode:
##b'helloeveryone'
##reading via r mode:
##b'helloeveryone'
'''


#?
'''
import pickle
data=[1,2,3,5,6]

c=pickle.dumps(data)
print(data,c)
f=open('binary3.txt','wb')
f.write(c)
f.close()

f=open('binary3.txt','rb')
print(f.read())
print(pickle.loads(c))
f.close()
'''


