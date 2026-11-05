#single level inheritance
'''
class HeadOffice:
    ceo='CEO'
    total_emp=123
    
class Branch(HeadOffice):
    dept_head='HEAD'
    

vijaynagar=Branch()
'''

#single level inheritance
'''
class Vehicle:
   brand='suzuki'
   fuel_type='petrol'

   def start(self):
       print('Vehicle is starting')

class Bike(Vehicle): #withotu inheritance! :(
    model='abc'
    yom=2025
    price=100000
    fuel_type='diesel' #overrides
    
    def ride(self):
        print('going on a bike ride')

u1=Bike()

print(u1.model)
print(u1.brand)

print(u1.fuel_type)

u1.ride()
u1.start()


'''

'''
#Multi level inheritance
#without using super()
# doubt -? - cant we do the follwoing using sql ? instead of creating methods for operations?
class Resume_10:
   
   def __init__(self,name,yop_10,per_10,sname_10,board_10):
      self.name=name
      self.yop_10 = yop_10
      self.per_10 = per_10
      self.sname_10 = sname_10
      self.board_10 = board_10

   #to dispaly we need object method
   def display_10(self):
      print('---10 class details:---')
      print(self.name,self.yop_10,self.per_10,self.sname_10,self.board_10,sep='\n')


class Resume_12(Resume_10):

   def __init__(self, name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12):
      #reinitialize parent class constructor attirbtues as init of child class overrides parent class init
      self.name=name
      self.yop_10 = yop_10
      self.per_10 = per_10
      self.sname_10 = sname_10
      self.board_10 = board_10
      
      self.yop_12=yop_12
      self.per_12=per_12
      self.sname_12=sname_12
      self.board_12=board_12

   def display_12(self):
      print('---12 class details:---')
      print(self.yop_12,self.per_12,self.sname_12,self.board_12,sep='\n')

class Resume_degree(Resume_12):

   def __init__(self, name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12,yopc,perc,cname,cuni):
      #reinitialize parent class constructor attirbtues as init of child class overrides parent class init
      self.name=name
      self.yop_10 = yop_10
      self.per_10 = per_10
      self.sname_10 = sname_10
      self.board_10 = board_10
      
      self.yop_12=yop_12
      self.per_12=per_12
      self.sname_12=sname_12
      self.board_12=board_12

      self.yopc=yopc
      self.perc=perc
      self.cname=cname
      self.cuni=cuni

   def display_degree(self):
      print('---Degree details:---')
      print(self.yopc,self.perc,self.cname,self.cuni)

#shreya = Resume_10('Shreya',2021,96,'Baldwin Girls HS','ICSE')

#shreya.display_10()

shreya = Resume_degree('Shreya',2021,96,'Baldwin Girls HS','ICSE',2023,96,'Sophia HS','ISC',2026,95,'MLACW','BCU')
shreya.display_10()
shreya.display_12()
shreya.display_degree()

   
'''
    
####


'''
#Multi level inheritance
# constructor chaining
# using super()
# thisprogram shows progress of 3 levels of resume where reusme at eahc level gets added 
# doubt -? - cant we do the follwoing using sql ? instead of creating methods for operations?
class Resume_10:
   
   def __init__(self,name,yop_10,per_10,sname_10,board_10):
      self.name=name
      self.yop_10 = yop_10
      self.per_10 = per_10
      self.sname_10 = sname_10
      self.board_10 = board_10

   #to dispaly we need object method
   def display_10(self):
      print('---10 class details:---')
      print(self.name,self.yop_10,self.per_10,self.sname_10,self.board_10,sep='\n')


class Resume_12(Resume_10):

   def __init__(self,name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12):
      #reinitialize parent class constructor attirbtues as init of child class overrides parent class init
      super().__init__(name,yop_10,per_10,sname_10,board_10)
      
      self.yop_12=yop_12
      self.per_12=per_12
      self.sname_12=sname_12
      self.board_12=board_12

   def display_12(self):
      print('---12 class details:---')
      print(self.yop_12,self.per_12,self.sname_12,self.board_12,sep='\n')

class Resume_degree(Resume_12):

   def __init__(self, name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12,yopc,perc,cname,cuni):
      #reinitialize object properties of parent class using super()

      super().__init__( name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12)

      self.yopc=yopc
      self.perc=perc
      self.cname=cname
      self.cuni=cuni

   def display_degree(self):
      print('---Degree details:---')
      print(self.yopc,self.perc,self.cname,self.cuni)

#shreya = Resume_10('Shreya',2021,96,'Baldwin Girls HS','ICSE')
#shreya.display_10() 

shreya = Resume_degree('Shreya',2021,96,'Baldwin Girls HS','ICSE',2023,96,'Sophia HS','ISC',2026,95,'MLACW','BCU')

shreya.display_10()
shreya.display_12()
shreya.display_degree()
    
'''



####


#Multi level inheritance
# method chaining - display
# using super() function
# thisprogram shows progress of 3 levels of resume where reusme at eahc level gets added 
# doubt -? - cant we do the follwoing using sql ? instead of creating methods for operations?
class Resume_10:
   
   def __init__(self,name,yop_10,per_10,sname_10,board_10):
      self.name=name
      self.yop_10 = yop_10
      self.per_10 = per_10
      self.sname_10 = sname_10
      self.board_10 = board_10

   #to dispaly we need object method
   def display(self):
      
      print('---10 class details:---')
      print(self.name,self.yop_10,self.per_10,self.sname_10,self.board_10,sep='\n')


class Resume_12(Resume_10):

   def __init__(self,name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12):
      #reinitialize parent class constructor attirbtues as init of child class overrides parent class init
      super().__init__(name,yop_10,per_10,sname_10,board_10)
      
      self.yop_12=yop_12
      self.per_12=per_12
      self.sname_12=sname_12
      self.board_12=board_12

   def display(self):
      super().display()
      print('---12 class details:---')
      print(self.yop_12,self.per_12,self.sname_12,self.board_12,sep='\n')

class Resume_degree(Resume_12):

   def __init__(self, name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12,yopc,perc,cname,cuni):
      #reinitialize object properties of parent class using super()

      super().__init__( name,yop_10,per_10,sname_10,board_10, yop_12,per_12,sname_12,board_12)

      self.yopc=yopc
      self.perc=perc
      self.cname=cname
      self.cuni=cuni

   def display(self):
      super().display()
      print('---Degree details:---')
      print(self.yopc,self.perc,self.cname,self.cuni)

#shreya = Resume_10('Shreya',2021,96,'Baldwin Girls HS','ICSE')
#shreya.display_10() 

shreya = Resume_degree('Shreya',2021,96,'Baldwin Girls HS','ICSE',2023,96,'Sophia HS','ISC',2026,95,'MLACW','BCU')

shreya.display()
