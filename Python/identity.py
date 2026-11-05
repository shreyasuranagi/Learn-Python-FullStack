'''a=(1,2,3)
b=(1,2,3)
print(a is b)
print(id(a),id(b))

l1=[1,2,3]
l2=[1,2,3]
print(id(l1),id(l2))
print(l1 is l2)'''

# a='10+5j'
# b='10+5j'
# print(a is b)
# print(id(a),id(b))


# d1={1:2,3:4}
# d2={1:2,3:4}
# print(d1 is d2)
# print(id(d1),id(d2))

print("identity operators- IS - file")
print("immutable data types ")

print("integer")
n=10
m=10
print(n is m)
print(id(10), id(10))

print(-10 is -10)
print(-10 is 10)

print()
print("float")
f1=10.5
f2=10.5
print(f1 is f2)
print(id(10.5), id(10.5))

print(id(0.1+0.2) is id(0.3))
print(0.2+0.3 is 0.5)

print()
print("complex")
c1=10+5.0j
c2=10+5j
print(c1 is c2)
print(id(10+5j), id(10+5j))

print(c1)