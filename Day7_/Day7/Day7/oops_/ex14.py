# Error Solved .
#Multiple Inheritance
# Method overriding
#Method overloading
class Father:
    def __init__(self,fname):
        self.__fname=fname
    def skills(self):
        print("I enjoy gardening",self.__fname)

class Mother:
    def __init__(self,mname):
        self.mname=mname
    def skills(self):
        print("I love cooking",self.mname)
    

class Child(Mother,Father):
    def __init__(self,mname,fname,name):
        Father.__init__(self, fname)
        Mother.__init__(self, mname)
        self.name=name
    def  skills(self):
        Mother.skills(self)
        Father.skills(self)
        
        print("I enjoy sports",self.name)
 
c=Child('Maa',"Paa","Mee")
c.skills()
