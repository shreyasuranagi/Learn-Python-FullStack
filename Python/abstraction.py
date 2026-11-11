#abstraction
'''
from abc import ABC, abstractmethod

class ATM(ABC):

    #def __init__(self,accno,bal):
    #no constructor
    #we cannot create object of abstract class as it has no implementation

    
    @abstractmethod
    def checkbal():
        pass

    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def withdraw():
        pass

    def change_pin():
        pass

ob=ATM()
#if class ATM() -> no error, still instantiates, NOT an abstract class
#if class ATM(ABC) -> cant instantiate as it is now an abstract class
'''

#############
'''
#this is a normal class:

class ATM:
    def checkbal():
        pass
'''

###################

'''
#this class is still a normal class only-
from abc import ABC, abstractmethod
class ATM:
    def checkbal():
        pass
'''
###############

'''
#abstract class without abstract method
from abc import ABC, abstractmethod
class ATM(ABC):
    def checkbal():
        pass
ob=ATM()
'''

###############


from abc import ABC, abstractmethod

class ATM(ABC):

    #def __init__(self,accno,bal):
    #no constructor
    #we cannot create object of abstract class as it has no implementation

    
    @abstractmethod
    def checkbal():
        pass

    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def withdraw():
        pass

    @abstractmethod
    def change_pin():
        pass

#ob=ATM()

class newATM(ATM):

    def __init__(self,name,accno,pin,bal):
        self.name=name
        self.accno=accno
        self.pin=pin
        self.bal=bal
    
    def checkbal(self):
        pin=input('Enter your pin:')
        if pin==self.pin:
            print('Balance : ',self.bal)
        else:
            print('Invalid pin')

    def deposit(self):
        
        pin=input('Enter your pin:')
        if pin==self.pin:
            amount=input('Enter amount to deposit:')
            
            self.bal += amount
            print('Deposited successfully')
        else:
            print('Invalid pin')

    def withdraw(self):

        pin=input('Enter your pin:')
        if pin==self.pin:
            amount=input('Enter amount to withdraw:')
            if amount>self.bal:
                self.bal = self.bal - amount
                print('Withdrawn successfully')
            print('Deposited successfully')
        else:
            print('Invalid pin')

    def change_pin(self):

        pin=input('Enter your pin:')
        if self.pin==pin:
            newpin=eval(input('Enter pin to change to:'))
            self.pin=newpin
            print('pin updated successfully')
        else:
            print('Invalid pin')
    

         
print('enter 1 to check balance')
print('enter 2 to update pin')
print('enter 3 to withdraw')
print('enter 4 to deposit')
print('enter 5 to stop')

def operations(obj):
    while True:
        choice=int(input('enter your choice:'))
        if choice==1:
            obj.check_bal()
        elif choice==2:
            obj.change_pin()
        elif choice==3:
            obj.withdraw()
        elif choice==4:
            obj.deposit()
        elif choice==5:
            print('exiting')
            break


c1=newATM('anu',2345,2345,123456)   
operations(c1)