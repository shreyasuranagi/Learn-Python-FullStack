Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,5,2]
l
[1, 2, 5, 2]
>>> #unpacking via indexing
>>> l[3]
2
>>> a,b,c,d=l[0],l[1],l[2],l[3]
>>> a
1
>>> b
2
c
>>> 
>>> d
2
>>> 
>>> #unpacking via independent variabels and packed variables
>>> 
>>> l
[1, 2, 5, 2]
>>> a,*b,c=l
>>> b
[2, 5]
>>> 
>>> #unpacking using multiple variabel assignment
>>> a,b,c,d=l
>>> a
1
>>> b
2
>>> c
5
>>> d
2
