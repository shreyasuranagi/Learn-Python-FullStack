#encapsulation -

class Bank:
    #class attributes
    bname='ICICI'
    manager='mr.Kiran'

    def __init__(self,name,accno):
        self.name=name
        self.accno=accno

    def display(self):
        print(self.name,self.accno)

print(Bank('abc',123)) #gives refernce address of the bank obj whic it has ust no created

    
