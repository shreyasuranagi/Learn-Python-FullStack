Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
d={1:1,2:4,3:9,4:16}
d
{1: 1, 2: 4, 3: 9, 4: 16}
type(d)
<class 'dict'>
dict()
{}
bool({})
False
bool(dict())
False
bool({1:1})
True

#dictionary lookup method
d[3]
9
d[6]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d[6]
KeyError: 6

#ccreate new value
d[6]=36
d
{1: 1, 2: 4, 3: 9, 4: 16, 6: 36}

#heterogeneous
>>> d1={1:3, 1.3:1.3, 'ab':4, (34,'1',2):[34,'l',2)}
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> d1={1:3, 1.3:1.3, 'ab':4, (34,'1',2):[34,'l',2]}
>>> d1
{1: 3, 1.3: 1.3, 'ab': 4, (34, '1', 2): [34, 'l', 2]}
>>> 
>>> 
>>> #assigning new value
>>> d[2]=2
>>> d
{1: 1, 2: 2, 3: 9, 4: 16, 6: 36}
>>> d[True]=0
>>> d
{1: 0, 2: 2, 3: 9, 4: 16, 6: 36}
>>> 
>>> #keys cannot be mutable types
>>> d2={1:2,{1,2}:4}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d2={1:2,{1,2}:4}
TypeError: unhashable type: 'set'
>>> d1[(32,'l',2)]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d1[(32,'l',2)]
KeyError: (32, 'l', 2)
>>> d1[(34,'l',2)]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d1[(34,'l',2)]
KeyError: (34, 'l', 2)
>>> d[(34,'1',2)]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d[(34,'1',2)]
KeyError: (34, '1', 2)
>>> d1[(34,'1',2)]
[34, 'l', 2]
