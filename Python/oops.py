'''
class Human:
    eyes=2
    mouth=1


a=Human()
b=Human()

#access class properties
print('acess using class name eyes:',Human.eyes,'mouth:',Human.mouth)
#print('access using class properties non-existent attribtues:',Human.ears) #error

#access object properties
print('access using object name eyes:',a.eyes,'mouth:', a.mouth)

#initialize new class properties - ? how it works in memory?
Human.ears=2

#class properties on all objects
print('New attribute for human ears:',Human.ears)
print('New attribute ears for a and b as well:',a.ears,b.ears)

#type
print(type(Human))
print(type(a))

#initialize new object properties
a.legs=2
print(a.legs)
#print(Human.legs) #error


#we can also access object method using class-
# oname.method()
# cname.method(oname,...)


'''





'''
#object properties
a.age=21
a.ph=456789
a.addr='bluru'

#access obj prop
print(f'a with phone{a.ph} live in {a.addr} and is {a.age} years old')
#print(b.addr)

Hitha=Human()
Hitha.name='Hitha'
Hitha.fruit='jackfruit'
Hitha.genre='horror'
Hitha.actor='Dhanveer'
Hitha.color='wine'
Hitha.dress='Western'
Hitha.song='melody songs'

'''


#template to create multiple objects at same time
'''
class Person:
    role='Student'
    lang='english'

    def __init__(o,age,course,ph):
        o.age=age
        o.course=course
        o.ph=ph

Shreya=Person(21,'bca',23456)
Hitha=Person(21,'bca',456789)
Pallavi_mam=Person(16,'be',456789)
Pallavi_mam.role='Trainer'

print(f'Shreya is {Shreya.age} years old, completed {Shreya.course} and is {Shreya.role}')
print(f'Hitha is {Hitha.age} years old, completed {Hitha.course} and is {Hitha.role}')
print(f'Pallavi mam is {Hitha.age} years old, completed {Pallavi_mam.course} and is {Pallavi_mam.role}')        
    
'''



#school object
#name princi place

#st name, st addr, standard

'''
class School:
    school_name='Sophia High School'
    school_principal='Sister Alpana'
    school_addr='Bengaluru'

    def __init__(self,name,std,section,addr,contact,grade,class_teacher):
        self.name=name
        self.std=std
        self.section=section
        self.addr=addr
        self.contact=contact
        self.grade=grade
        self.class_teacher=class_teacher

    def print_details(self):
        self.static_print()
        print(self.name,self.std,self.section,self.addr,self.contact,self.grade,self.class_teacher,self.school_name)
        print(id(self))

    #class method
    #withotu decorator it is taking address of object
    #with decortator it ALWAYS takes address of class, evne if we call it with objct or class cos using obj-> it finds addreess of class
    @classmethod
    def update_principal(cls,new):
        cls.school_principal=new

    #object method
    def update_std(self,new):
        self.std=new

    #static method
    @staticmethod
    def static_print():
        print('The details of the student are:')

anya=School('Anya',3,'b','malleshwaram',567890,'a+','Mrs.Jayalatha')
tanya=School('Tanya',4,'c','malleshwaram',234234,'c','Mrs.Monica')
arya=School('Arya',5,'a','jpnagar',876765,'b+','Mrs.Pramila')
sanya=School('Sanya',6,'d','malleshwaram',23134,'a+','Mrs.Vandana')



#RecursionError: maximum recursion depth exceeded -   [Previous line repeated 1023 more times]

#to avoid this below repeated code we use object method - print_details

#print(anya.name,anya.std,anya.section,anya.addr,anya.contact,anya.grade,anya.class_teacher)
#print(tanya.name,tanya.std,tanya.section,tanya.addr,tanya.contact,tanya.grade,tanya.class_teacher)
#print(sanya.name,sanya.std,sanya.section,sanya.addr,sanya.contact,sanya.grade,sanya.class_teacher)


anya.print_details()
tanya.print_details()

anya.update_std(4)
anya.print_details()

School.update_principal
tanya.update_principal('shreya')



'''


#BANK
'''

class Bank:
    name='SBI'
    location='Vijaynagar'

    def __init__(self,name,accno,aadhar,addr):

        self.name=name
        self.accno=accno
        self.aadhar=aadhar
        self.addr=addr
        self.balance=0

    def display_details(self):
        print(f'Name:{self.name}, AccNo:{self.accno}, Aadhar:{self.aadhar}, Address:{self.addr}, Balance:{self.balance}')

    def deposit(self):
        amount=int(input('Enter deposit amount:'))
        self.balance = self.balance + amount
        print(f'Deposited Rs.{amount} successfully')
        
    def check_bal(self):
        print(f'Customer name: {self.name}, AccNo: {self.accno}, Balance:{self.balance}')

    def withdraw(self):
        amount=int(input('Enter withdraw amount:'))
        if amount<=self.balance:
            self.balance= self.balance - amount
            print(f'Withdrew Rs.{amount} successfully')
        else:
            print(f'Invalid: cannot Withdraw more than balance!')
    
    
anya=Bank('Anya',1234567,23456234,'Bengaluru')
arya=Bank('Arya',12343437,239834,'Mysuru')

anya.display_details()
anya.deposit()
anya.display_details()

arya.display_details()
arya.deposit()
arya.display_details()

anya.check_bal()
arya.check_bal()

anya.withdraw()
anya.check_bal()

arya.withdraw()
arya.check_bal()

'''       


    



