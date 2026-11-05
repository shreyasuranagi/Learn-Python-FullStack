class Shop:
    total_shops=0
    def __init__(self,name,location,stock):
        self.name=name
        self.location=location
        self.stock=stock
        Shop.total_shops += 1

    def display(self):
        print(self.name,self.location,self.stock,end=' ')
        print()

    @classmethod
    def total_shops_count(cls):
        print('Total shops:',cls.total_shops)

    def update_stock(self,newstock):
        self.stock=newstock
        print('Newstock:',self.stock)

    @staticmethod
    def discount_info():
        print('---DEEPAVALI OFFER ON OUR STORES---')
        print('Discounts: Wholesale: 10%, Online: cashback rs.200 for orders above Rs.1000, Supermarket:get rewards for purchase baove rs.500')

    
    

class Wholesale(Shop):
    def __init__(self,name,location,stock,product,staff):
        super().__init__(name,location,stock)
        self.product=product
        self.staff=staff


class Online(Shop):
    def __init__(self, name,website,stock,ids,delivery_persons):
        super().__init__(name,website,stock)
        self.ids=ids
        self.delivery_persons=delivery_persons

    def display(self):
        super().display()
        print(self.ids,self.delivery_persons)
        print()
        

class Supermarket(Shop):
    def __init__(self,name,location,stock,categories,employees):
        super().__init__(name,location,stock)
        self.categories=categories
        self.employees=employees

    def display(self):
        super().display()
        
        print(self.categories,self.employees)
        print()


s=Supermarket('Reliance','Vijaynagar',1450,['fruits','vegetables','snacks','dairy'],35)
s.discount_info()
s.display()

Shop.total_shops_count()

o=Online('AMazon','www.amazon.com',10000,'am123',2435)
o.display()

Shop.total_shops_count()
Shop.discount_info()

w=Wholesale('Kitchenware store','Malleshwaram',4590,'Kitchenware',30)
w.display()

Shop.total_shops_count()

w.update_stock(11000)
w.display()




