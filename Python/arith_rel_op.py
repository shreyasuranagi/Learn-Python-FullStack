Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators - math and relational

#operator types = arith, relational, logical, bitwise, membership, dientity, assignment

#math - add, sub, mul, div-true,floor,modulus, exponent/power
#relational - ==, !=, >,<, >=, <=

#arithmetic operator

#addition -
# supports all svd
# for collection data type it acts as concatenation operator - ecept for set, dict which throws an error

#svd - operands cna be of any data type
#collection - operands must of same data type

3+4
7
-4+2
-2
3.5+3.3
6.8
3+3.3
6.3
4.0+3
7.0
5+False
5
3.5+5+True
9.5
3+10.22222222222222222227
13.222222222222221
3.0+10.22222222222222222227
13.222222222222221
1.0+2.0
3.0
(2+1j)+3
(5+1j)
2+0j+3.5j
(2+3.5j)
0j+3+2j
(3+2j)
[1,2,3]+[1,2,6]
[1, 2, 3, 1, 2, 6]
[1,2,'hi',(12,4)]+[1,4.3]
[1, 2, 'hi', (12, 4), 1, 4.3]
[1,2,3]+(1,2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    [1,2,3]+(1,2)
TypeError: can only concatenate list (not "tuple") to list
(1,2)+(1,)
(1, 2, 1)
{1,2}+{1,2}
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    {1,2}+{1,2}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1:2,3:4}+{2:5}
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    {1:2,3:4}+{2:5}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
'h'+'ello'
'hello'



'hey'+123
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    'hey'+123
TypeError: can only concatenate str (not "int") to str
[1,2,4]+3
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    [1,2,4]+3
TypeError: can only concatenate list (not "int") to list


########################################

#multiplication
#supports all svd, and any data type
#for colelction any one operan msut be int only, set and dict not supported
3*6
18
3.4*9.0
30.599999999999998
3.4*9.1
30.939999999999998
(1+1j)*(1+1j)
2j
True*3
3
3.3*2
6.6

[1,2,3]*[1,2]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    [1,2,3]*[1,2]
TypeError: can't multiply sequence by non-int of type 'list'
[1,2,3]*3.5
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    [1,2,3]*3.5
TypeError: can't multiply sequence by non-int of type 'float'
[1,2,3]*2
[1, 2, 3, 1, 2, 3]
(1,23)*4
(1, 23, 1, 23, 1, 23, 1, 23)
'ha ha'*3
'ha haha haha ha'


##################

#division
#supports only svd and NOT colleciton data types
#/-true-completely divides, returns quotiesnt ith decimal part, as a  float value
3.3/3.3
1.0
2/3
0.6666666666666666
5/True
5.0
3/3
1.0
(2+3j)(2+34j)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    (2+3j)(2+34j)
TypeError: 'complex' object is not callable
(2+3j)/(2+4j)
(0.8-0.1j)
2/(2+3j)
(0.3076923076923077-0.46153846153846156j)
[1,2,3]/3
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    [1,2,3]/3
TypeError: unsupported operand type(s) for /: 'list' and 'int'


2//3
0
4//3
1
3.5//3.5
1.0
6.//3.2
1.0
12/3.4
3.5294117647058822
12//3.4
3.0
(2+3j)//3
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    (2+3j)//3
TypeError: unsupported operand type(s) for //: 'complex' and 'int'

3*2
6
3%2
1
23.5%2.3
0.5000000000000018
1.5%2
1.5
1%3j
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    1%3j
TypeError: unsupported operand type(s) for %: 'int' and 'complex'
[1,2,3]%2
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    [1,2,3]%2
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> 
>>> 
>>> 
>>> #####################################
>>> 
>>> #relational
>>> 
>>> 3.0=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 3.0==3
True
>>> [1,2,3]==(1,2,3)
False
>>> l=[1,2,3]
>>> tuple(l)==(1,2,3)
True
>>> 'hello=="hello"
SyntaxError: unterminated string literal (detected at line 1)
>>> 'hello'=="hello"
True
>>> {1,2,3}={3,2,1}
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?
>>> {1,2,3}=={3,2,1}
True
>>> 
>>> 
>>> 'bye'>'Bye'
True
>>> ord('B')
66
>>> [1,2,3]>[1,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> [1,2,3]>[1,3]
False
