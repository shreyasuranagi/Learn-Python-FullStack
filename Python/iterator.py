#iterator
'''
l={1:2,3:4} #only iterable
#next(l) #cannot traverse /iterate over an ierable, ONLY on iterator

d=iter(l)
print(d) #<list_iterator object at 0x0000021156A59FF0>

print(next(d))
print(next(d))
#print(next(d))
#print(next(d)) #StopIteration
'''


#generator
'''

def sam():
    
    a=10
    b=20
    return a+b
    return a-b
    print('hi')
    return a*b

print(sam())

'''


'''
def sam2():
    
    a=10
    b=20
    yield a+b
    yield a-b
    print('hi')
    yield a*b

print(sam2())
print(list(sam2()))
#hi
#[30, -10, 200]

i=iter(sam2())
#30
#-10
#hi

print(next(i))
print(next(i))
print(next(i))
'''

def sam2():
    
    a=10
    b=20
    yield a+b
    print('hello')
    yield a-b
    
    print('hi')
    return
    yield a*b

print(sam2())
print(list(sam2()))
#hi
#[30, -10, 200]

i=iter(sam2())

print(next(i))
print(next(i))
#print(next(i))
'''
30
hello
-10
hi
'''


#generator expression
'''
import sys

gen=(i for i in range(1,100))
comp=[i for i in range(1,10000)]

print(sys.getsizeof(gen))
print(sys.getsizeof(comp))

'''

