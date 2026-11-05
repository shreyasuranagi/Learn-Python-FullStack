Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t=(1,5,2,5)
>>> t.count(5)
2
>>> t.index(2)
2
>>> t.count(0)
0
>>> s='today day'
>>> s.count('day')
2
>>> 
>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s={1,5,2}
>>> s
{1, 2, 5}
>>> s.copy()
{1, 2, 5}
s1=s.copy()
s1
{1, 2, 5}
s1={2,4,3.5,1,6}
s1
{1, 2, 3.5, 4, 6}
s2={3.5,1,7,8}
s2
{8, 1, 3.5, 7}
s1
{1, 2, 3.5, 4, 6}
s2
{8, 1, 3.5, 7}
s1-s2
{2, 4, 6}
s1.difference(s2)
{2, 4, 6}


s1.difference_update(s2)
s1
{2, 4, 6}
s2
{8, 1, 3.5, 7}
s1
{2, 4, 6}
s1={2,4,3.5,1,6}
s2={3.5,1,7,8}
s1.difference(s2)
{2, 4, 6}
s1
{1, 2, 3.5, 4, 6}
s1.difference_update(s2)
s1
{2, 4, 6}



s1={2,4,3.5,1,6}
s1
{1, 2, 3.5, 4, 6}
s2={3.5,1,7,8}
s2
{8, 1, 3.5, 7}
s1.difference(s2)
{2, 4, 6}
s1
{1, 2, 3.5, 4, 6}
s2.difference_update(s2)
s1.difference_update(s2)
s1
{1, 2, 3.5, 4, 6}
s2
set()
help(differnce_update)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    help(differnce_update)
NameError: name 'differnce_update' is not defined
help(difference_update)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    help(difference_update)
NameError: name 'difference_update' is not defined
help(set.difference_update)
Help on method_descriptor:

difference_update(self, /, *others) unbound builtins.set method
    Update the set, removing elements found in others.

s1
{1, 2, 3.5, 4, 6}
s1.remove(2)
s1
{1, 3.5, 4, 6}
s1.remove()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s1.remove()
TypeError: set.remove() takes exactly one argument (0 given)
s1.pop()
1
s1
{3.5, 4, 6}
s1
{3.5, 4, 6}
s1.discard(3.5)
s1
{4, 6}
s1.discard(100)
s1
{4, 6}
s1.discard()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s1.discard()
TypeError: set.discard() takes exactly one argument (0 given)
help(set.discard)
Help on method_descriptor:

discard(self, object, /) unbound builtins.set method
    Remove an element from a set if it is a member.

    Unlike set.remove(), the discard() method does not raise
    an exception when an element is missing from the set.

s1={1,2,3}
s2={2,3,5,6}
s1
{1, 2, 3}
s2
{2, 3, 5, 6}
s1-s2
{1}
s1
{1, 2, 3}
s1&s2
{2, 3}
s1
{1, 2, 3}
s2
{2, 3, 5, 6}
s1.intersection(s2)
{2, 3}
s1
{1, 2, 3}
s2
{2, 3, 5, 6}
s1.intersection_update(s2)
s1
{2, 3}
s2
{2, 3, 5, 6}
s2.intersection_update(s1)
s2
{2, 3}
s1
{2, 3}
s1={1,2,4}
s2={4,6,2,3}
s1
{1, 2, 4}
s2
{2, 3, 4, 6}
s2=(2,6,3,5,1,4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
s2={2,6,3,5,1,4}
s2
{1, 2, 3, 4, 5, 6}
s1
{1, 2, 4}
s1.isdisjoint(s2)
False
s1={4,6,2,5}
s2={4,5,2,9}
s
{1, 2, 5}
s1
{2, 4, 5, 6}
s2
{9, 2, 4, 5}
s1.subset(s2)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s1.subset(s2)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?


s1={1,2,3,4,5}
s2={2,3}
s1.subset(s2)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    s1.subset(s2)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
s1.issubset(s2)
False
s2.issubset(s2)
True
s2.issubset(s1)
True


s1= {1,2,3,4,5}
s2={2,3,6,7}
s1
{1, 2, 3, 4, 5}
s2
{2, 3, 6, 7}
s1.symmetric_difference(s2)
{1, 4, 5, 6, 7}
s1
{1, 2, 3, 4, 5}
s1.symmateric_difference_update(s2)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    s1.symmateric_difference_update(s2)
AttributeError: 'set' object has no attribute 'symmateric_difference_update'. Did you mean: 'symmetric_difference_update'?
s1.symmeteric_difference_update(s2)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s1.symmeteric_difference_update(s2)
AttributeError: 'set' object has no attribute 'symmeteric_difference_update'. Did you mean: 'symmetric_difference_update'?
s1.symmetric_difference_update(s2)
s1
{1, 4, 5, 6, 7}
s1
{1, 4, 5, 6, 7}
s2
{2, 3, 6, 7}
p=s1.symmetric_difference(s2)
p
{1, 2, 3, 4, 5}
q=s1.symmetric_difference_update(s2)
q


s1.union(s2)
{1, 2, 3, 4, 5, 6, 7}
s1
{1, 2, 4, 5, 3}
s1.update(s2)
s1
{1, 2, 3, 4, 5, 6, 7}
