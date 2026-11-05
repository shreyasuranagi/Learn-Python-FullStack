#packing  - processing of combining multiple values and storing into a single collection

#type 1 - implicit packing - tuple by default
#type 2 - argument packing - *args, **kwargs - tuple and dict
#type 3 - starred expression using multiple variable assignment - list'

#type 1 - implicit tuple packing
a=1,2,3
print(a) #(1,2,3) by default


#type 2 - argument packing

#type 2a - *args - single/tuple packing
#packs positional arguments into a tuple using *args as parameter in the function defintion - creates a tuple



#type 2b - **kwargs - double/dict packing
#packs keywrod arguments into a dictionary using **kwargs as parameter in the function defintion - creates a dict


def s(a,b,c,d,name,std):
    print('total:',a+b+c+d)
    print(f'name: {name}, std:{std}')

s(10,50,20,30,std=10,name='abc')


def s(*args, **kwargs): #here it is always packing
    print(*args) #here it is UNPACKING the multiple values in args tuple. using the *
    #print(type(*args)) #error - type take 1 ro 3 arguments (here getting 4)

    print()

    print(args) #(10,50,20,30)
    print(type(args))

    print()
    print(kwargs)
    print(type(kwargs))
    d={**kwargs}  #how to unpack dictionary
    print(d)
    #print(**kwargs)  #errror cos unpakcing adicionary gives key value pairs that cnanot be printed by print()

    #unpack *args
    marks=args
    total=0
    for i in marks:
        total+=i
        
    print('total:', total)

    
    
    #print(f'name: {**kwargs[name]}, std:{**kwargs[std]}')
    print(f'name: {kwargs[name]}, std:{kwargs[std]}')
s(10,50,20,30,std=10,name='abc')

###########
my_dict = {'name': 'xyz', 'tot': 100}

# Unpacking a dict gives you its keys
a, b = my_dict
print(a)  # Output: 'name'
print(b)  # Output: 'tot'
    
