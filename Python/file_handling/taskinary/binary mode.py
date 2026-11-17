
# assignment
#p7-wb+

#create new testicon output file
f=open('testicon.jpg','ab+')

#to confirm where the file pointer is
print(f.tell())

#open existing image file and read its data into capture
f1= open('capture.jpg','rb')
capture=f1.read()

#open another bigger image file and read its data into icon
f2= open('icon.jpg','rb')
icon=f2.read()

#write it into the output file
f.write(icon)
#f.seek(4000)
print(f.tell())

#write another image over it
f.write(capture)
print(f.read())
f.close()

#close other files

f2.close()
f1.close()



#####################

'''
# assignment
#p7-wb+

#create new testicon output file
f=open('testext.txt','ab+')

#to confirm where the file pointer is
print(f.tell())

#open existing image file and read its data into capture
f1= open('capture.jpg','rb')
capture=f1.read()

#open another bigger image file and read its data into icon
f2= open('icon.jpg','rb')
icon=f2.read()

#write it into the output file
f.write(capture)
#f.seek(4000)
print(f.tell())

#write another image over it
f.write(capture)
print(f.read())
f.close()

#close other files

f2.close()
f1.close()
'''


######################################
##############################################
'''

#rb+
import pickle
print('write binary plus mode--')
f=open('rb.txt','wb+')
f.write(b'hello there\n')
f.writelines([b'here is some\n',b'binary data in text\n'])
binary=pickle.dumps('this line is converted by pickle')
f.write(binary)
f.seek(0)
print(f.read())
f.seek(0)
f.write(b'overwriting data')
print('after overwritin--')
f.seek(0)
print(f.read())
f.close()

#output-
#b'hello there\nhere is some\nbinary data in text\n\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00\x8c this line is converted by pickle\x94.'


#wb+
import pickle
print()
print('read binary plus mode---')
f=open('rb.txt','rb+')
print(f.readline())
print(f.readline())
print(f.readline())

f.seek(0)
f.readline()
f.readline()
last=pickle.loads(f.read())
print(last)

print('lets write onw--')
print(f.write(b'binary is a torture'))
f.seek(0)
print('printing from start--')
print(f.read())
f.close()




#ab+

import pickle
print()
print('append binary plus mode---')
f=open('rb.txt','ab+')
print(f.readline())

f.seek(0)
f.write(b'APPENDING SOME LINES')
print(f.readline())
print(f.readline())
f.seek(0)
print(f.read())
f.close()
#output- no use, always adds to end of file
'''

#========================

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
