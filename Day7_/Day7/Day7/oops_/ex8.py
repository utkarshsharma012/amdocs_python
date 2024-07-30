#Simple Inheritance
class Vehicle:
    var=90
    def general_usage(self):
        print("general use: transporation")

class Car(Vehicle):
    var=56
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print(self.var,Vehicle.var)#56,90
        self.general_usage()
        print("specific use: commute to work, vacation with family")

c=Car()
print(c.wheels)
print("=======From inside specific_usage=======")
c.specific_usage()
print("=======End=======")
c.general_usage()
print(c.var)#56
print(Vehicle.var)#90


