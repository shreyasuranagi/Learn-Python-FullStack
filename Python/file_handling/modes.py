#write mode - w
'''
open('file1.txt','w')
f.write('hi\n')

f.writelines(['hi','hello\n','namaskara'])
f.close()
'''


'''
f=open('file1.txt','w')
f.close()
'''


#error- #read mode - r
'''
try:
    f=open('file2.txt','r')
except:
    print('file not found ')

f.close()
'''

#read mode - r
'''
try:
    f=open('file1.txt','r')
except:
    print('file not found ')
else:
    print(f.readlines()) #['hello\n', 'world it is\n', 'Friday today!']
    #print(f.readline())
    #print(f.readline())
    #f.close() #error- ValueError: I/O operation on closed file.

##
##hello
##world it is
##Friday today!

##hello # becuae pyhton is adding newline at \n
##
##world it is
'''


'''
f=open('file1.txt')
print(f.read(7))
f.close()
'''

#append mode - a
'''
f=open('file1.txt','a')
f.write('and today is MOnday!')
f.write('\n hi again')
f.close()

'''


#x mode
'''

f=open('file2.txt','x')
f.write('x mdoe writing\n')
f.close()
'''


######################
#unsupported Operation

# +  modes



#w+ mode - both write and read
'''
f=open('file2.txt','w+')
print(f.tell()) #0
#f.writelines(['Python today\n','no JS class today\n'])
print(f.tell()) #0
f.seek(5)
print(f.readline())
print(f.tell()) #5
print(f.readline())
print(f.tell()) #5
f.close() 
'''

'''
f=open('file2.txt','w+')
print(f.tell()) #0
#f.writelines(['Python today\n','no JS class today\n'])
print(f.tell()) #33
f.seek(5)
print(f.readline()) # n today
print(f.tell()) #14
print(f.readline()) #no JS class today
print(f.tell()) #33
f.close() 
'''


'''
f=open('file1.txt','w+')
print(f.tell()) #0
f.writelines(['Python today\n','no JS class today\n'])
print(f.readline())
print(f.tell()) #33
f.writelines(['Python today\n','no JS class today\n'])
#f.seek(5)
print(f.readline()) # n today
print(f.tell()) #14
print(f.readline()) #no JS class today
print(f.tell()) #33
f.close()
'''



#lets say i want to start reading from the first vowel position in file

#f=open('file2.txt','w+')



# r+
'''
f=open('file2.txt','r+')
print(f.read())
f.close()
'''

###########################################
###########################################
# practice test.txt

#p1-r
'''
f=open('test.txt','r')
print(f.readline())
print(f.tell())
f.seek(2)
#f.write('hello') # io.UnsupportedOperation: not writable
print(f.tell())
print(f.read())
f.close()


##seek tell works with  r mode.
##cant write, onyl read. reading starts at 0
##
##input-
##kjh
##sdfw
##erw
##
##output-
##kjh
##
##5
##2
##h
##sdfw
##erw

'''




#p2-w
'''
f=open('test.txt','w')
print(f.write('kitten'))
f.close()

f=open('test.txt','w')
print(f.write('hello world')) #5 ??
print(f.tell())
f.seek(2)
print(f.write('abc'))
print(f.tell())
f.seek(0)
print(f.write('cat'))
print(f.tell())
#print(f.read()) io.UnsupportedOperation: not readable
f.close()
'''

'''
write mode starts at 0 index
overwrites whole file if used without seek
if used with seek(0) then it overwrite sonly few charss only
seek and tell also work in w mode


input-
hello world

output-
catbc world
6
11
11
3
5
3
3
'''

#p3-a
'''
f=open('test.txt','a')
print(f.write('kitten'))
f.close()

f=open('test.txt','a')
print(f.write('hello world')) 
print(f.tell())
f.seek(2)
print(f.write('abc'))
print(f.tell())
f.seek(0)
print(f.write('cat'))
print(f.tell())
print(f.read()) # io.UnsupportedOperation: not readable
f.close()



##appned mode seek wont work, alwaysat end of file
##
##
##input-
##kjh
##sdfw
##erw
##
##output-
##kjh
##sdfw
##erwkittenhello worldabccat
##6
##11
##31
##3
##34
##3
##37

'''


#p4 - w+
'''
f=open('test.txt','w+')
print(f.read())
print(f.tell())
f.write('abc')
f.write('defg\n')
f.write('hi')
print(f.tell())
print(f.read())
print(f.seek(4))
print(f.readline())
print(f.write('123'))
f.close()
'''

'''
abcdefg
hi123

output-

0
11

4
efg

3

'''



#p5 - r+
'''
f=open('test.txt','r+')
print(f.write('hey'))
print(f.tell())
print(f.read())
print(f.tell())
print(f.seek(5))
print(f.read())
f.close()
'''


#p6-a+
'''
f=open('test.txt','a+')
print(f.tell())
print(f.write('added'))
print(f.tell())
print(f.seek(0))
print(f.tell())
print(f.readline())
print()
f.close()
'''

# assignment
#p7-wb+

f=open('testb.txt','wb+')
print(f.tell())
f1= open('icon.jpg','rb')
icon=f1.read()
print(icon)
f.write(icon)
s1=b'hello there testing here'
f.write(s1)
f1.close()
f.close()


'''

f=open('testb.txt','wb+')
print(f.tell())

s1=b'hello there testing here'
f.write(s1)
s2='non binary string'
f.write(s2.encode())
f.close()
'''


'''
import pickle
f=open('testb.txt','wb+')
print(f.tell())

s1=b'hello there testing here'
outs1=pickle.dumps(s1)
f.write(outs1)
s2='non binary string'
f.write(s2.encode())
f.seek(1)
print(f.read())
f.close()
'''




'''
with open("testb.txt", "rb") as file:
  loaded_data = pickle.load(file)
  print(loaded_data)

with open('testb.txt','ab+') as file:
    file.write(b'[1,2,3]')
    file.seek(0)
    print(file.tell())
    print(file.read())
    print(pickle.load(file))
'''
