'''
def instagram(func):
    
    def wrapper(*args,**kwargs):
        print('go to website')
        print('login')
        func(*args,**kwargs)
        print('logout')
    return wrapper
    

@instagram
def Nikhila(name):
    print('text with',name)

def Nandhika(name):
    print('make reels with',name)

Nikhila('Divyani')

Nandhika ('Apeksha')

'''



'''
#without wrapper??

def instagram(func):
    
    def wrapper(*args,**kwargs):
        print('go to website')
        print('login')
        func(*args,**kwargs)
        print('logout')
    return wrapper
    
    print('go to website')
    print('login')
    func(name) #name args is not defined
    print('logout')

@instagram
def Nikhila(name):
    print('text with',name)

def Nandhika(name):
    print('make reels with',name)

Nikhila('Divyani')

Nandhika ('Apeksha')
'''


#create a decorator to calculate execution time fir any proggram
'''
import time

def time_duration(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        print('duration:',end-start)
    return wrapper
@time_duration
def is_prime1(n):
    c=0
    for i  in range(1,n+1):
        if n%i==0:
            c+=1

    
    print(c==2)
    
@time_duration
def is_prime2(n):
    
    c=0
    for i  in range(1,int(n**0.5)+1):
        if n%i==0:
            c+=1

    
    print(c==2)

(is_prime1(981))
(is_prime2(981))


(is_prime1(37))
(is_prime2(37))

(is_prime1(98764567))
(is_prime2(98764567))

#37 and 981 almomst similar in prime2 method
'''

#wap to give thedely tie of 5s before executing tha mian task
'''
import time


def delay5(func):
    def wrapper(*args,**kwargs):
        
        time.sleep(5)
        func(*args,**kwargs)
        
    return wrapper
@delay5
def wait():
    print('done waiting')
wait()

'''

#wap count how any time  a function is called

'''
def count(func):
    c=0
    def wrapper(*args,**kwargs):
        nonlocal c 
        
        func(*args,**kwargs)
        c+=1
        print('function called for ',c,'no of times')
        
    return wrapper
@count
def rain():
    for i in range(10):
        print('it is raining')
rain()
rain()
rain()


# 1. rain() is called BUT it has a decorator so the count function is
# actually FIRST called as follows by passing the count: var=count(rain())
# 2. count creates nonlocal variable c accessed by count and wrapper
# 3. now wrapper def is executed so wrapper is only created it in memory say -0x11
# 4. that wrapper address 0x11 is returned
# 5. now var=0x11 executes
# 6. nonlocal c...rain()...c+=1..print()..
# 7. next time it is called rain() since c is non local c is not 0 again -?
# need of wrapper class??
'''
