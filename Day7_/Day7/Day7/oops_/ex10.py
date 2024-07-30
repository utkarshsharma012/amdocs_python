#Multilevel Inheritance
class Father:
    def gardening(self):
        print("I enjoy gardening")

class Mother(Father):
    def cooking(self):
        print("I love cooking")

class Child(Mother):
    def  skills(self):
        print("I enjoy sports")

c=Child()
c.skills()
c.gardening()
c.cooking()