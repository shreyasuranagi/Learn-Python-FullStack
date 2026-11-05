Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,5,2,3,6,3)
t
(1, 5, 2, 3, 6, 3)
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
t.count(3)
2
t.count(100)
0
t=('abc',10,'abc',3.5)
t
('abc', 10, 'abc', 3.5)
t.count('ab')
0
t=([1,2,3],2,4,{1,2,3},[1,2,3],2)
t
([1, 2, 3], 2, 4, {1, 2, 3}, [1, 2, 3], 2)
t.count([1,2,3])
2
([1, 2, 3], 2, 4,{1:2,3:4}, {1, 2, 3}, [1, 2, 3], 2,{1:2,3:4})
([1, 2, 3], 2, 4, {1: 2, 3: 4}, {1, 2, 3}, [1, 2, 3], 2, {1: 2, 3: 4})
>>> ([1, 2, 3], 2, 4,{1:2,3:4}, {1, 2, 3}, [1, 2, 3], 2,{1:2,3:4}).count({1:2,3:4})
2
>>> (True,0,1,True,-1).count(1)
3
>>> (True,0,1,True,-1).count(True)
3
>>> t1=(2,3,4)
>>> (3,1,5,2,3,4,(2,3,4),56,5).count(t1)
1
>>> t=([1,2,3],2,4,{1,2,3},[1,2,3],2)
>>> t.index(2)
1
>>> t.index([1,2,3])
0
>>> t.index(5)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t.index(5)
ValueError: tuple.index(x): x not in tuple
>>> help(tuple.index)
Help on method_descriptor:

index(self, value, start=0, stop=9223372036854775807, /) unbound builtins.tuple method
    Return first index of value.

    Raises ValueError if the value is not present.

>>> 
======================= RESTART: C:/Users/Suranagi/Desktop/Python/user_defined_functions.py ======================
