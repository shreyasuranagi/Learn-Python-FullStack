
>>> #keywords
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> #no. of keywords
>>> len(keyword.kwlist)
35
>>> 
>>> #keywords with internal values -> special keywords: True, False, None

