#hybrid inheritance

class Person:
    def __init__(self,name,ids,role,phno):
        self.name=name
        self.ids=ids
        self.role=role
        self.phno=phno

    def display(self):
        self.printtable()
        print(self.name,self.ids,self.role,self.phno,end=' ',sep='\t')

    @staticmethod
    def printtable():
        print('Name \t id \t role \t phno \t Dept \t Manager \t Employee_list')
   
        
class Employee(Person):
    def __init__(self,name,ids,role,phno,dept,manager):
        super().__init__(name,ids,role,phno)
        self.dept=dept
        self.manager=manager

        
        
    def display(self):
        #self.printtable()
        super().display()
        print(self.dept,self.manager,end=' ',sep='\t')
        print()

class Manager(Employee):
    def __init__(self,name,ids,role,phno,dept,manager,employees_list):
        super().__init__(name,ids,role,phno,dept,manager)
        self.employees_list=employees_list
        if manager!=None: #if is not the ceo
            self.assign_employees_to_manager(manager)

    def assign_employees_to_manager(self,manager):
        if manager not in self.employees_list:
            manager.employees_list.append(self.name)
        self.manager= (self.manager).name
        

    def display(self):
        #self.printtable()
        super().display()
        print(self.employees_list,sep='\t')
        print()
    

class Customer(Person):
    def __init__(self,name,ids,role,phno):
        super().__init__(name,ids,role,phno)

    def display(self):
        #self.printtable()
        super().display()

ceo=Manager('ceo nita','C000','ceo',78987654,'Pentagon ',None,[])
ceo.display()


m1=Manager('Mr.ravi','M123','manager',2345678,'IT',ceo,[])
ceo.display()
m1.display()


e1=Employee('sita','E123','employee',8768765,'IT',m1)
e1.display()
m1.display()
'''
e2=Employee('priti','E153','employee',654678,'IT',m1)


m2=Manager('Ms.sheela','M263','manager',2345678,'Sales','ceo nita',[])

e3=Employee('ramu','E253','employee',463478,'Sales',m2)



c =Customer('Somu','C123','customer',3456789)

e1.display()
e2.display()
m.display()
c.display()
'''

##

'''
another idea-

company->hr/resource + billing/budget (mutltiple) -> it + social media (hierarchcial)

'''

