class details:
    print("This is details class")
    var=0
    def __init__(self,email="admin@test.com",name="Raj",mobileno=798547):
        print("This is __init__ method.",email)
        self.email=email
        self.name=name
        self.mobileno=mobileno
        self.data=True
    
#     def __repr__(self): 
    def __str__(self):
        return f"User(name:- {self.name}, email:- {self.email})"
        
    def out(self):
        print(self.email)
        
if __name__=="__main__":
    obj1=details("Test@gmail.com","Manish",898585547)
    print(obj1)
    obj2=details()
    print(obj2)
