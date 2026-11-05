Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#type casting

#int -> ?
#int->int
a=3
type(a)
<class 'int'>
int(a)
3
#no change, no use

#int->float
float(a)
3.0
float(-1)
-1.0
float(0)
0.0

#int->complex
complex(a)
(3+0j)
complex(0)
0j

complex(a,a)
(3+3j)
complex(a,-10)
(3-10j)
complex(a,0)
(3+0j)
complex(5,2.3)
(5+2.3j)
complex(1,2,3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex(1,2,3)
TypeError: complex() takes at most 2 arguments (3 given)


#int->str
str(a)
'3'
str(complex(a,a))
'(3+3j)'
str(-12423)
'-12423'

#int to any other colleciton type excdpt str is not possible
list(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable


###########################################

#float->?

#float->int
a=10.23
int(a)
10
b=-4.98
int(b)
-4

#float->float - no use, same output

#float->complex
complex(b)
(-4.98+0j)
complex(a,b)
(10.23-4.98j)
complex(0.0)
0j
complex(3.412345678901234567890)
(3.4123456789012345+0j)
str(b)
'-4.98'
str(complex(b))
'(-4.98+0j)'
len(str(complex(b)))
10


#float-> any other collection type has no purpose
list(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable



##############################################

#complex-> ?
a=3+4j
#complex->bool
bool(a)
True
bool(0+0j)
False
bool(0j)
False
str(a)
'(3+4j)'
len(str(a))
6
#above was bool->str
#complex->complex no use


#####################################################

#type conversion for bool
#bool -> ?

#bool->int
bool(0)
False
bool(1)
True
bool(False)
False
bool(True)
True

#bool->float
bool(1.0)
True
bool(0.0)
False


b=True
b1=False
int(b)
1
int(b1)
0
float(b)
1.0
float(b1)
0.0
complex(b)
(1+0j)
complex(b1)
0j
bool(b)
True
bool(b1)
False
str(b)
'True'
len(str(b))
4

#other values not possible/no purpose to other collection types
list(b)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
dict(b1)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    dict(b1)
TypeError: 'bool' object is not iterable


#################################################################

#str -> ?
#str->int

s='abcd'
s
'abcd'
int(s)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'abcd'
int('abc')
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    int('abc')
ValueError: invalid literal for int() with base 10: 'abc'
int('123')
123
float('12.4')
12.4
complex('0+3j')
3j
complex('2.3+2j')
(2.3+2j)
complex('j')
1j
complex('5')
(5+0j)


bool('')
False
bool(s)
True
str(s)
'abcd'
list(s)
['a', 'b', 'c', 'd']
tuple(s)
('a', 'b', 'c', 'd')
set(s)
{'a', 'b', 'd', 'c'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
s='(a,b),(c,d)'
dict(s)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required


#################################

s='123'
complex(s)
(123+0j)
complex(s,s)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    complex(s,s)
TypeError: complex() can't take second arg if first is a string
#error -> complex like changing j value so ony we cant pass 2 arguments

s='j'
str(s)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    tr(s)
NameError: name 'tr' is not defined. Did you mean: 'str'?



##################################

#type casting for list

l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]

int(l)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
bool(l)
True
bool('')
False
str(l)
'[1, 2, 3, 4, 5]'
len(l)
5
len(str(l))
15
list(l)
[1, 2, 3, 4, 5]
tuple(l)
(1, 2, 3, 4, 5)
l=[12,34,'hi',[1,2]]
str(l)
"[12, 34, 'hi', [1, 2]]"
list(l)
[12, 34, 'hi', [1, 2]]
tuple(l)
(12, 34, 'hi', [1, 2])
set(l)
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    set(l)
TypeError: unhashable type: 'list'
l=[1,2,3,4]
set(l)
{1, 2, 3, 4}
dict(l)
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
d=[[1,2],{2,4},(2,3),'me']
d
[[1, 2], {2, 4}, (2, 3), 'me']
dict(d)
{1: 2, 2: 3, 'm': 'e'}
#important above


#############################################

#tuple->?
#type casting for tuple
t=(1,20,34,12,56)
int(t)
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
f
float(t)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
bool(t)
True
bool(())
False
str(t)
'(1, 20, 34, 12, 56)'
list(t)
[1, 20, 34, 12, 56]
tuple(t)
(1, 20, 34, 12, 56)
dict(t)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
t=((1,2),[3,4],'by')
dict(t)
{1: 2, 3: 4, 'b': 'y'}


#####################################
#type casting of dictionary

d={1:2,3:3,4:5,5:6}
d
{1: 2, 3: 3, 4: 5, 5: 6}
int(d)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
bool(d)
True
bool({})
False
str(d)
'{1: 2, 3: 3, 4: 5, 5: 6}'
len(str(d))
24
list(d)
[1, 3, 4, 5]
tuple(d)
(1, 3, 4, 5)
dict(d)
{1: 2, 3: 3, 4: 5, 5: 6}
set(d)
{1, 3, 4, 5}


>>> ###################################
>>> #set
>>> s={1,2,3,4,2}
>>> s
{1, 2, 3, 4}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
>>> bool(s)
True
>>> bool({}
...      )
False
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> str(s)
'{1, 2, 3, 4}'
>>> list(s)
[1, 2, 3, 4]
>>> tuple(s)
(1, 2, 3, 4)
>>> set(s)
{1, 2, 3, 4}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
