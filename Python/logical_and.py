Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #logical operators
>>> #and operator
>>> 
>>> True and False
False
>>> True and True
True
>>> 10<5 and 12<30
False
>>> 5<10 and 12<3.5
False
>>> 12>3.7 and 2+3j>2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    12>3.7 and 2+3j>2
TypeError: '>' not supported between instances of 'complex' and 'int'
>>> 10 and 11
11
>>> a=10
>>> a-10 and a+13
0
>>> 'hi' and 123
123
>>> 0.0 and 0
0.0
>>> [] and ''
[]
>>> '' and [
...     ]
''
>>> ' ' and []
[]
