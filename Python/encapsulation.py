#encapsulation
'''
class Bank:
    bname='SBI'
    __branch='Vijaynagar' #private
    _manager='mr.ravi'#protected
    ifsc='sbi110031'

    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.__phno=phno #private
        self.accno=accno
        self._bal=bal  #protected

    @classmethod
    def display(cls): #cls refers to the address of class always by default
        print(cls.bname,cls.branch,cls._manager,cls.ifsc)

class Bank2(Bank):

    #protected members must be accessible here - > manager, balance
    def __init__(self,name,phno,accno,bal):
        super().__init__(name,phno,accno,bal)
        
    def display(self):
        #print(self,self.bname, self.__branch,self._manager)
        print(self.name,self._bal,self._Bank2__phno,self._manager) #name mangling   for phno
    

c1 = Bank('Laskhmi',9876543,3456789998765,10000000000)
c2 = rBank2('abc',2345,345,12345)
'''


##############
#OUTPUTS of the above
'''

Bank.manager
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Bank.manager
AttributeError: type object 'Bank' has no attribute 'manager'
Bank._manager
'mr.ravi'
c1.bal
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    c1.bal
AttributeError: 'Bank' object has no attribute 'bal'
c1._bal
10000000000

'''



'''


Bank.branch
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Bank.branch
AttributeError: type object 'Bank' has no attribute 'branch'
Bank.__branch
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Bank.__branch
AttributeError: type object 'Bank' has no attribute '__branch'
Bank._Bank__branch
'Vijaynagar'


#name mangling-

c1.phno
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c1.phno
AttributeError: 'Bank' object has no attribute 'phno'
c1.__phno
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c1.__phno
AttributeError: 'Bank' object has no attribute '__phno'
c1._Bank__phno
9876543


'''


#getter and setter methods


class Bank:
    bname='SBI'
    __branch='Vijaynagar' #private
    _manager='mr.ravi'#protected
    ifsc='sbi110031'

    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.__phno=phno #private
        self.accno=accno
        self._bal=bal  #protected

    @classmethod
    def display(cls): #cls refers to the address of class always by default
        print(cls.bname,cls.__branch,cls._manager,cls.ifsc)

        #print(cls.bname,cls.branch,cls.manager,cls.ifsc)   #AttributeError: type object 'Bank' has no attribute 'branch'
       
        #NOT NAME mangling, but accessing directly since while executin it is inside class anyway
        #if i need to access branch and manager inside >> window(outside class) -> __branch etc wont work well need name mangling in that window
        
    '''
    #1-normal syntax cannot access this phno private member outside class
    def get_phno(self):
        print(self.phno) 
        #
        #AttributeError: 'Bank' object has no attribute 'phno'
    '''
    
        
    '''
    #1 - directly outside the class using c1._Bank__phno - name mangling
    #2 - getter method
    
    def get_phno(self):
        print(self.__phno)

    '''
    
    #3 - decorators
    
    @property
    def phno(self):
        print(self.__phno)
        
    #3 - decorators
    @phno.setter
    def phno(self,new):
        self.__phno=new

    
    
    

c1 = Bank('Laskhmi',9876543,3456789998765,10000000000)
c1.display()
#c1.phno(1234)


