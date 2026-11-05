def positional(name,addr,phone):
    print('name:',name)
    print('phone:',phone)
    print('addr:',addr)

positional('Shreya',123567890,'bluru')

'''
def default(name,phone1, , phone2=None,addr='Mysuru'):
    print('name:',name)
    print('addr:',addr)
    print('phone1:',phone1)
    print('phone2:',phone2)
default('Shreya','Bluru',234)
'''
'''
def default(name,phone1, addr='Mysuru', phone2=None):
    print('name:',name)
    print('addr:',addr)
    print('phone1:',phone1)
    print('phone2:',phone2)
default('Shreya','Bluru',234)
'''
'''
def keyword(name,addr,phone):
    print('name:',name)
    print('addr:',addr)
    print('phone1:',phone1)
keyword(addr='bluru',23456789,name='Shreya')
'''

def sargs(*args):
    print(args)
sargs(2,4.5,'c','af')

def dsargs(**kwargs):
    print(kwargs)
dsargs(item='milk',cost='42')

def dsargs(**d):
    print(d)
dsargs(item='milk',cost='42')
