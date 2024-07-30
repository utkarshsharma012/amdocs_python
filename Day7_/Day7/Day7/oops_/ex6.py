class details:
    print("This is details class")
    var=0
    def __init__(self,email="admin@test.com",name="Raj",mobileno=798547):
        print("This is __init__ method.",email)
        self.email=email
        
    def out(self):
        print(self.email)
        

obj1=details("Test@gmail.com","Manish",898585547)
print(obj1)
obj2=details()
print(obj2)
obj1.out()
