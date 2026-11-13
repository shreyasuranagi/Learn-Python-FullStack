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


#error-
'''
#read mode - r

try:
    f=open('file2.txt','r')
except:
    print('file not found ')

f.close()
'''

#read mode - r

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


