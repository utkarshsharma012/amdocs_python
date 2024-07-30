class vehicles:
    def __init__(self):
        self.Data=True
    def out(self,name,color,type,price):
        print(f"{name} is a {color} {type} worth ${(price)}")
        
car1=vehicles()
car1.out("Fer","red","convertible",60000)
car2=vehicles()
car2.out("Jump","blue","van",10000)