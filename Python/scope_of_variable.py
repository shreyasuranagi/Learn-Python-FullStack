#scope of variables

#global -1

'''
#global 1-
a=10
b=20
print(a,b) #10,20
def f():
    print(a,b) #access global var  10,20
f()
a=40 #global can be modified in global scope 
print(a,b) #global can be accessed anywhere + modification outside function(in global scope) affects - 40, 10

print('='*30)
'''

#global 2-
'''
#global vars cos defined outside of function
a=10
b=20
print(a,b) #10, 20
def f():
    #print(a,b) #error - cannot access local variable 'a' where it is not associated with a value
    
    #cos Pyhton first looks for a local variable and it s a compile time issue
    #to fix it - use global keyword
    
    a=30  #global variable cannot be modified inside local scope, it creates a new local variable(variable shadowing)
    print(a,b) #global can be accessed anywhere - 30,20
f()
print(a,b) #modifications in local scope not affected - 10,20

print('='*30)
'''

#global keyword
'''
#global vars cos defined outside of function
a=10
b=20
print(a,b) #10, 20
def f():
    #print(a) #errorocmpile- a is used befroe is ti sdeclared global
    #a=30  #global variable cannot be modified inside local scope, it creates a new local variable(variable shadowing)
    
    #fix - globla keyword
    global a
    
    a=30
    print(a,b) #global can be accessed anywhere - 30,20
f()
print(a,b) #modifications in local scope not affected - 30,20

print('='*30)
'''

#local-1
'''
a=10
b=20
print(a,b) #10,20
def f():
    x=30 #local
    y=40
    print(x,y) #local variables can be accessed inside local scope/inside function - 30,40
    x=60  #local variable can be modified inside local scope
    print(x,y) #local can be accessed in local - 60,40
    print(a,b) #10,20
f()
print(x,y) #NameError: name 'x' is not defined
#ERror- local cannot be accessed in global scope/outside function

print('='*30)
'''


#enclosing-1
'''
a=10
b=20
print(a,b) #10,20
def outer():
    x=30 #enclosing
    y=40
    print(a,b) #10,20
    print(x,y) #30,40
    x=50
    def inner():
        print(a,b) #10,20
        print(x,y) #50,40 
        m=80
        n=90
        print(m,n) #80, 90
        
    inner()
    
    #print(m,n) #Error - m not defined - local var cannot be accessed outside its function
    print(x,y) #50,40
    
print()

outer()
'''


#enclosing scope - 2
'''
a=10
b=20
print(a,b) #10,20
def outer():
    x=30 #enclosing
    y=40
    print(a,b) #10,20
    print(x,y) #30,40
    x=50
    def inner():
        print(a,b) #10,20
        print(x,y) #50,40 UnboundLocalError - Compiler: cannot access local variable 'x' where it is not associated with a value
        #compiler expects x is local var so looks for it becos of the x=60 initialsiation down
        #fix it using nonlocal
        m=80
        n=90
        print(m,n) #80, 90
        x=60
    inner()
    
    #print(m,n) #Error - m not defined - local var cannot be accessed outside its function
    print(x,y) #60,40
    
print()

outer()
'''
  
#nonlocal
'''
a=10
b=20
print(a,b) #10,20
def outer():
    x=30 #enclosing
    y=40
    print(a,b) #10,20
    print(x,y) #30,40
    x=50
    def inner():
        nonlocal x #converts local scope x to enclosing - uses x from the enclosing scope
        print(a,b) #10,20
        print(x,y) #50,40 
        m=80
        n=90
        print(m,n) #80, 90
        x=60
    inner()
    
    #print(m,n) #Error - m not defined - local var cannot be accessed outside its function
    print(x,y) #60,40
    
print()

outer()
'''

#enclosin 3
'''
a=10
b=20
print(a,b) #10,20
def outer():
    #enclosing
    y=40
    print(a,b) #10,20
    
    def inner():
        nonlocal x #error- no binding for x -> since x is not declared in enclosign scop e we cnanoe concvert x to nonlocal
        # also we cnanot jsut eclare a variable
        #converts local scope x to enclosing - uses x from the enclosing scope
        print(a,b) #10,20
        x=50
        print(x,y) #50,40 
        m=80
        n=90
        print(m,n) #80, 90
        x=60
    inner()
    
    #print(m,n) #Error - m not defined - local var cannot be accessed outside its function
    print(x,y) #60,40
    
print()
outer()
'''





#FINAL - each scope :- declaration, access, modification
#global - declaration, access, modification

'''
a=100
print(a)
def f():
    print(a)
    a=200
    print(a)
f()
print(a)
'''

#local - declaration, access, modification
'''
def f():
    a=10
    print(a)
    a=20
    print(a)
f()
#print(a)
'''

#enclosing - declaration, access, modification
'''
def outer():
    
    oa=1
    print(oa)
    oa=2
    print(oa)

    def inner():
        ob=3
        print(ob)
        ob=4
        print(ob)
    inner()
outer()
'''


#all scopes
'''
# Complete working program demonstrating Global, Enclosing, and Local scopes
# along with global and nonlocal keywords.

# 1. GLOBAL SCOPE
a = 10
b = 20
print(a, b)  # 10, 20

def outer():
    # 2. ENCLOSING SCOPE
    x = 30
    y = 40
    print(a, b)  # 10, 20 (Accessing global variables)
    print(x, y)  # 30, 40 (Accessing enclosing variables)
    
    def inner():
        # 3. LOCAL SCOPE
        nonlocal x  # Points to 'x' from the enclosing scope (outer)
        global a    # Points to 'a' from the global scope
        
        print(a, b)  # 10, 20 (Accessing global/enclosing)
        
        # Modifying global and enclosing variables
        a = 15       # Modifies global 'a' from 10 to 15
        x = 50       # Modifies enclosing 'x' from 30 to 50
        
        print(x, y)  # 50, 40 (Modified enclosing x, normal enclosing y)
        
        # Purely local variables
        m = 80
        n = 90
        print(m, n)  # 80, 90
        
    inner()
    
    # m and n are local to inner(), so they cannot be accessed here (Error if tried)
    # print(m, n) 
    
    # Notice: 'x' is now 50 because inner() modified it using 'nonlocal'!
    print(x, y)  # 50, 40

print()
outer()

# Notice: 'a' is now 15 because inner() modified it using 'global'!
print(a, b)  # 15, 20
'''

#all scopes - game
'''
# ==========================================
# 1. GLOBAL SCOPE
# ==========================================
score = 100
game_title = "Python Quest"

print(f"--- GLOBAL SCOPE ---")
print(f"Game: {game_title}, Initial Score: {score}\n")


def outer_function():
    # ==========================================
    # 2. ENCLOSING SCOPE
    # ==========================================
    level = 5
    gold = 50
    
    print(f"--- ENCLOSING SCOPE (outer_function) ---")
    print(f"Starting Level: {level}, Starting Gold: {gold}\n")
    
    def inner_function():
        # ==========================================
        # 3. LOCAL SCOPE
        # ==========================================
        local_weapon = "Magic Wand"
        
        # Access and modify the GLOBAL variable using 'global'
        global score
        score += 50  # Modifies the global score from 100 to 150
        
        # Access and modify the ENCLOSING variable using 'nonlocal'
        nonlocal gold
        gold += 25   # Modifies outer_function's gold from 50 to 75
        
        print(f"--- LOCAL SCOPE (inner_function) ---")
        print(f"Local weapon: {local_weapon}")
        print(f"Modified Global Score (via 'global'): {score}")
        print(f"Modified Enclosing Gold (via 'nonlocal'): {gold}\n")
        
    # Run the inner function
    inner_function()
    
    print(f"--- BACK IN ENCLOSING SCOPE ---")
    print(f"Level is still: {level} (untouched)")
    print(f"Gold is now: {gold} (changed by inner_function via 'nonlocal')\n")


# Run the outer function
outer_function()

print(f"--- BACK IN GLOBAL SCOPE ---")
print(f"Final Global Score is now: {score} (changed by inner_function via 'global')")
'''

