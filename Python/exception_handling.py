# eception handling
# sepcific exception handling
'''
try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    print(a/c)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print('enter only int')
finally:
    print('completed execution')
'''

# what if error statemtn is outisde of try block

'''
try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    
except NameError:
    print('ending due to error')

except ValueError:
    print('enter only int')
else:
    print(a+c)
finally:
    print('execution completed')    print('execution completed')
'''


# generic exception handling
'''
try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    print(a/b)
except Exception as e:
    print(e)
else:
    print('no error')
finally:
    print('done executing')
'''


# KeyboardInterrupERror not handled by eenerice xception handling
'''
try:
    for i in range(1,1000):
        print(j)
except Exception as e:
    print(e)
except KeyboardInterrupt as e:
    print(e)
    print('keyboard input given by user')
else:
    print('no error')
finally:
    print('done executing')
'''


'''
135
136
137
138
done executing
Traceback (most recent call last):
  File "C:/Users/Suranagi/Desktop/Learn Python FullStack/Python/exception_handling.py", line 56, in <module>
    print(i)
KeyboardInterrupt
'''


'''
try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    print(a/b)
except Exception as e:
    print(e)
except KeyboardInterrupt as e: #better to write more specific error
    print(e)
    print('keyboard input given by user')
else:
    print('no error')
finally:
    print('done executing')
'''    


'''
try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    print(a/b)
except Exception as e:
    print('uh oh')
except ValueError as e: #better to write more specific error  first
    print('nooo')
else:
    print('no error')
finally:
    print('done executing')
'''


# Bare exception
'''
try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    print(a/b)
    for i in range(1,1000):
        print(i)
except:
    print('something went wrong')
else:
    print('no error')
finally:
    print('--ending--')
'''

'''
try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    print(a/b)
except:
    print(a/2)
else:
    print('no error')
finally:
    print('--ending--')
'''




#create a NotPalindrome error and raise it if the str is not palindrome

'''
class NotPalindrome(Exception):
    pass

s=input('enter')

if (s!=s[::-1]):
    raise NotPalindrome(word,'it is not a palindrome')
else:
    print('Palindrome!!')

'''



# RAISING ERRORS
'''
try:
    n=int(input('enter:'))
except:
    print('error handled')
else:
    if n%2==0:
        print('even')
    else:
        try:
            raise ValueError('sorry but that is an odd number')
        
        finally:
            print('ending after handling')
'''

#ASSERTION ERROR
'''
n=int(input('enter:'))
assert n>0, 'it is negative, enter only positive'
print('it is positive:',n**2)
'''

#create abnk class with withdraw method and user enters amt to withdrraw, if amt>bal raise error
'''
class BalanceError(Exception):
    pass

class Bank:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def withdraw(self):
        amt=int(input('enter amount to withdraw'))
        
        if amt>self.balance:
            raise BalanceError('insuffiecient balance')
        else:
            self.balance=self.balance-amt
            print(f'withdrew Rs.{amt} successfully')
            
    def checkbal(self):
        print('Balance:',self.balance)

a=Bank('Ananya',100)
a.checkbal
a.withdraw()
a.checkbal()
'''



class BalanceError(Exception):
    pass

class Bank:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def withdraw(self):
        try:
            amt=int(input('enter amount to withdraw'))
        except ValueError as e:
            print(e)
            print('enter only valid amount')
        else:
            
            

            assert self.balance>amt,'balance low'
            self.balance=self.balance-amt
            print(f'withdrew Rs.{amt} successfully') 
            
    def checkbal(self):
        print('Balance:',self.balance)

a=Bank('Ananya',100)
a.checkbal
a.withdraw()
a.checkbal()

