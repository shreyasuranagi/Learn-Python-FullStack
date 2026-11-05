Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
t=(1,3,4.5,1'abc,[1,234,12,2])
   
SyntaxError: unterminated string literal (detected at line 1)
t=(1,3,4.5,1'abc'
   
SyntaxError: '(' was never closed
t=(1,3,4.5,1'abc',[1,234,12,2])
   
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t=(1,3,4.5,1,'abc',[1,234,12,2])
   
t
   
(1, 3, 4.5, 1, 'abc', [1, 234, 12, 2])
type(t)
   
<class 'tuple'>
id(t)
   
2066338646144
tuple()
   
()
bool(t)
   
True
bool(())
   
False



#indexing
   
t[3]
   
1
t[5]
   
[1, 234, 12, 2]
t[5][2]
   
12
t[4][1]
   
'b'
>>> 
>>> 
>>> #changing element
...    
>>> t[0]=-1
...    
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t[0]=-1
TypeError: 'tuple' object does not support item assignment
>>> 
>>> #length
...    
>>> len(t)
...    
6
>>> 
>>> t1=6
...    
>>> type(t1)
...    
<class 'int'>
>>> t1=(6)
...    
>>> type(t1)
...    
<class 'int'>
>>> t1=6,
...    
>>> type(t1)
...    
<class 'tuple'>
>>> t1=(6,)
...    
>>> type(t1)
...    
<class 'tuple'>
