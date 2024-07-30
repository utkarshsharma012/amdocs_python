#Multilevel Inheritance
# Method overriding
#Method overloading
class Father:
    def __init__(self,fname):
        self.fname=fname
    def skills(self):
        print("I enjoy gardening",self.fname)

class Mother(Father):
    def __init__(self,mname,fname):
        super().__init__(fname)# load the value into the __init__ method of Father class
        self.mname=mname
    def skills(self):
        print("I love cooking",self.mname)
        
# m=Mother('Ma',"Paa")
# Father.skills(m)


class Child(Mother):
    def __init__(self,mname,fname,name):
        super().__init__(mname, fname)
        self.name=name
    def  skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I enjoy sports",self.name)
 
c=Child('Maa',"Paa","Mee")
c.skills()
