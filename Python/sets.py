Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets

s={10,20,10,3.5,'hey'}
s
{10, 3.5, 'hey', 20}

type(s)
<class 'set'>
id(s)
2027684732864
set()
set()

bool(set())
False

#error-indexing is not supported
s[3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s[3]
TypeError: 'set' object is not subscriptable

s.add(95)
s
{3.5, 10, 'hey', 20, 95}
s.add([35,'cool',12.3])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.add([35,'cool',12.3])
TypeError: unhashable type: 'list'
s.add((35,'cool',12.3))
s
{3.5, 10, 'hey', (35, 'cool', 12.3), 20, 95}


s.add(356)
s
{3.5, 356, 10, 'hey', (35, 'cool', 12.3), 20, 95}
# adds to random positions


#update
s.add('sweets')
s
{3.5, 356, 10, 'hey', (35, 'cool', 12.3), 20, 'sweets', 95}
s.update('sweets')
s
{'w', 3.5, 356, 10, 'hey', (35, 'cool', 12.3), 20, 's', 'e', 't', 'sweets', 95}
len(s)
12
s.update(3)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.update(3)
TypeError: 'int' object is not iterable
s.update([6,5,4])
s
{'w', 3.5, 356, 5, 6, 4, 10, 'hey', (35, 'cool', 12.3), 20, 's', 'e', 't', 'sweets', 95}


#pop
s.pop()
'w'
s.pop
<built-in method pop of set object at 0x000001D81B6D9FC0>
>>> s.pop()
3.5
>>> s
{356, 5, 6, 4, 10, 'hey', (35, 'cool', 12.3), 20, 's', 'e', 't', 'sweets', 95}
>>> s.pop(3)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.pop(3)
TypeError: set.pop() takes no arguments (1 given)
>>> 
>>> #remove()
>>> s.remove('hey')
>>> s
{356, 5, 6, 4, 10, (35, 'cool', 12.3), 20, 's', 'e', 't', 'sweets', 95}
>>> s.remove((35,'cool',12.3))
>>> s
{356, 5, 6, 4, 10, 20, 's', 'e', 't', 'sweets', 95}
>>> s.remove(1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.remove(1)
KeyError: 1
>>> 
>>> #clear
>>> s.clear()
>>> s
set()
>>> s.pop()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.pop()
KeyError: 'pop from an empty set'
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s
NameError: name 's' is not defined
