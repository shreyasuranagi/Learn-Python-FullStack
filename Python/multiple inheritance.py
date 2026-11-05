# multiple inheritance

class Batsman:
    def __init__(self, name,team,age,runs,centuries):
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.centuries=centuries

    def bat(self):
        print(self.name,'is batting')
        return self

    def display(self):
        print(self.name,self.team,self.age,self.runs,self.centuries)

class Bowler:
    def __init__(self,name,team,age,wickets,dot_balls):
        self.name=name
        self.team=team
        self.age=age
        self.wickets=wickets
        self.dot_balls=dot_balls

    def bowl(self):
        print(self.name,'is bowling')
        return self

    def display(self):
        print(self.name,self.team,self.age,self.wickets,self.dot_balls)

class AllRounder(Batsman,Bowler):
    #by MRO it take s init method form Batsman first order
    #as we want form Bowler as wlel we need to create init class

    def __init__(self, name,team,age,runs,centuries,wickets,dot_balls):

        '''
        #super().__init__(name,team,age,runs,centuries) #works with Batsman cos by defualt calls first class
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.centuries=centuries
        #self.wickets=wickets
        #self.dot_balls=dot_balls
        '''

        '''
        super().__init__(name,team,age,runs,centuries) #works with Batsman cos by defualt calls first class
        super().__init__(name,team,age,wickets,dot_balls) # still calls Batsman due to MRO
        '''

        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.centuries=centuries
        self.wickets=wickets
        self.dot_balls=dot_balls
        

    def field(self):
        print(self.name,'is fielding')
        return self

    def display(self):
        super().display() #method chainngin - type 1 not possible either #by MRO it calls Batsman as it is first class

        

ob=AllRounder('Krunal Pandya','RCB',32,10000,100,300,5000)

print(ob.runs,ob.age,ob.centuries,ob.wickets,ob.dot_balls)
ob.display()
print(ob)
print(AllRounder.mro())
print(AllRounder.__mro__)

#method chaining
ob.field().bat().bowl()
