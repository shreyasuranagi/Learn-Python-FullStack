Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list functions

#list functions to add values to the list
#append() - adds only one value/ element to end of list
#insert(index, value) - adds one value/element at index
#extend(collection) - adds multiple values at the end of list

l=[1,4,'abc',3.5,[10,20,30],300]
l
[1, 4, 'abc', 3.5, [10, 20, 30], 300]
#append one value
l.append(5)
l
[1, 4, 'abc', 3.5, [10, 20, 30], 300, 5]

#append without value/with more than one values -> error
l.append()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.append()
TypeError: list.append() takes exactly one argument (0 given)
l.append(9,8,7)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l.append(9,8,7)
TypeError: list.append() takes exactly one argument (3 given)
l.append('def')
l
[1, 4, 'abc', 3.5, [10, 20, 30], 300, 5, 'def']


#insert(index,value) - at index. if index not there->end of list
l.insert(3,6)
l
[1, 4, 'abc', 6, 3.5, [10, 20, 30], 300, 5, 'def']
l.insert(100,6.5)
l
[1, 4, 'abc', 6, 3.5, [10, 20, 30], 300, 5, 'def', 6.5]
l.insert('ghi',5)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.insert('ghi',5)
TypeError: 'str' object cannot be interpreted as an integer
#try error - multiple values not accepted
l.insert(3,5,6,7)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l.insert(3,5,6,7)
TypeError: insert expected 2 arguments, got 4


#extend(collection)=/values) - at end of list
l.extend('jkl')
l
[1, 4, 'abc', 6, 3.5, [10, 20, 30], 300, 5, 'def', 6.5, 'j', 'k', 'l']
l[5].extend([40,50])
l
[1, 4, 'abc', 6, 3.5, [10, 20, 30, 40, 50], 300, 5, 'def', 6.5, 'j', 'k', 'l']
l.append(l[5])
l
[1, 4, 'abc', 6, 3.5, [10, 20, 30, 40, 50], 300, 5, 'def', 6.5, 'j', 'k', 'l', [10, 20, 30, 40, 50]]


#pop()
l.pop()
[10, 20, 30, 40, 50]
#l.pop(index)
l.pop(5)
[10, 20, 30, 40, 50]
l
[1, 4, 'abc', 6, 3.5, 300, 5, 'def', 6.5, 'j', 'k', 'l']

l.pop(100)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l.pop(100)
IndexError: pop index out of range

#remove(value) - removes specific value
l.remove(6)
l
[1, 4, 'abc', 3.5, 300, 5, 'def', 6.5, 'j', 'k', 'l']
l.append(4)
l
[1, 4, 'abc', 3.5, 300, 5, 'def', 6.5, 'j', 'k', 'l', 4]
#remove duplicates?
l.remove(4)
l
[1, 'abc', 3.5, 300, 5, 'def', 6.5, 'j', 'k', 'l', 4]
l.remove(100)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    l.remove(100)
ValueError: list.remove(x): x not in list
l.remove()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    l.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> 
>>> #clear
>>> l.clear()
>>> l
[]
>>> 
>>> #delete l
>>> del l
>>> l
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> 
>>> #nested list
>>> l=[1,3,11,[43,'adf',345,11,[23,4,23,'g'],23,1],345,11,'morning']
>>> l[3][4].pop()
'g'
>>> l
[1, 3, 11, [43, 'adf', 345, 11, [23, 4, 23], 23, 1], 345, 11, 'morning']
>>> len(l)
7
>>> l[6].pop()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    l[6].pop()
AttributeError: 'str' object has no attribute 'pop'
>>> l[3].remove(43)
>>> l
[1, 3, 11, ['adf', 345, 11, [23, 4, 23], 23, 1], 345, 11, 'morning']
>>> l[3].clear()
>>> l
[1, 3, 11, [], 345, 11, 'morning']
>>> l[3].extend("abcd")
>>> l
[1, 3, 11, ['a', 'b', 'c', 'd'], 345, 11, 'morning']
