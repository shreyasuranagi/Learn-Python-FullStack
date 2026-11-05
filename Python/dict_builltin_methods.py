Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
d={}
t=(1,2,3)
d.fromkeys(t)
{1: None, 2: None, 3: None}
d.copy()
{}
d
{}
d1=d.copy()
d1
{}
d=d.fromkeys(t)
d
{1: None, 2: None, 3: None}
d
{1: None, 2: None, 3: None}
d={1:2}
t=(1,2,4)
d
{1: 2}
t
(1, 2, 4)
d.fromkeys(t)
{1: None, 2: None, 4: None}
d
{1: 2}
d.fromkeys(t,10)
{1: 10, 2: 10, 4: 10}
d
{1: 2}
d1=dict.fromkeys(t,10)
d1
{1: 10, 2: 10, 4: 10}
d1
{1: 10, 2: 10, 4: 10}
d
{1: 2}
d=d.fromkeys(t)

d
{1: None, 2: None, 4: None}
d2=d.copy()
d2
{1: None, 2: None, 4: None}
d2.clear()
d2
{}
d2[6]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d2[6]
KeyError: 6
d[6]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d[6]
KeyError: 6
d[3]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d[3]
KeyError: 3
d[2]
d={1:2,2:3,4:5}
d
{1: 2, 2: 3, 4: 5}
d[2]
3
d[4]
5
d[10]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d[10]
KeyError: 10
d.get(10)
d.get(10,0)
0
d.items()
dict_items([(1, 2), (2, 3), (4, 5)])
d.pop()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.pop(3)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d.pop(3)
KeyError: 3
d.pop(3,100)
100
>>> d.pop('helo')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d.pop('helo')
KeyError: 'helo'
>>> d.pop(3,'helo')
'helo'
>>> d.values()
dict_values([2, 3, 5])
>>> 
>>> 
>>> 
>>> 
>>> d
{1: 2, 2: 3, 4: 5}
>>> d[2]
3
>>> d[2]=10
>>> d
{1: 2, 2: 10, 4: 5}
>>> d.setdefault(7,6)
6
>>> d
{1: 2, 2: 10, 4: 5, 7: 6}
>>> d.setdefault(2,11)
10
>>> 
>>> d
{1: 2, 2: 10, 4: 5, 7: 6}
