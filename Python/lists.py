Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#lists

simple_list=[2,3,'a',2.3]
simple_list
[2, 3, 'a', 2.3]

#type of list
type(simple_list)
<class 'list'>

#default value of list
list()
[]

#length of list
len(simple_list)
4

#address of list
id(simple_list)
1865823812992

#homgeneous list
homo = [2.3,.5, 5.664,1.]
homo
[2.3, 0.5, 5.664, 1.0]

#heterogeneous list
hetero=[1,3J+2.4,'a',7005,'lists']
hetero
[1, (2.4+3j), 'a', 7005, 'lists']

#nested list
n=['abcd',3.45234,'True',True, [2,4,'eight',10,''],4,[[.0,2,'sky'],[2],6],[]]
n
['abcd', 3.45234, 'True', True, [2, 4, 'eight', 10, ''], 4, [[0.0, 2, 'sky'], [2], 6], []]
#length of list
len(n)
8

#indexing
n[2]
'True'
n[3]
True
n[6]
[[0.0, 2, 'sky'], [2], 6]

#indexing
n[0][3]
'd'
n[4][4]
''
n[6][2][0]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    n[6][2][0]
TypeError: 'int' object is not subscriptable
>>> n[6][1][0]
2
>>> n[6][0][2][-1]
'y'
>>> n[-3][-3][2]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    n[-3][-3][2]
TypeError: 'int' object is not subscriptable
>>> n[-4][-3][2]
'g'
>>> 
>>> #memory address
>>> id(n)
1865784083648
>>> id(n[0])
1865794242384
>>> id(n[1])
1865774551120
>>> id(n[2])
140723126630880
>>> id(n[-1])
1865784083584
>>> 
>>> #error situation - changing a string which is immutable
>>> n[0][2]='d'
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    n[0][2]='d'
TypeError: 'str' object does not support item assignment
>>> 
>>> #no error -changing elements of a list -> lists are mutable
>>> n[0]=100
>>> n
[100, 3.45234, 'True', True, [2, 4, 'eight', 10, ''], 4, [[0.0, 2, 'sky'], [2], 6], []]
>>> 

#checking edit
n
