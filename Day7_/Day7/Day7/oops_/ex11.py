#Multilevel Inheritance
# Method overriding
class Father:
    def skills(self):
        print("I enjoy gardening")

class Mother(Father):
    def skills(self):
        print("I love cooking")

class Child(Mother):
    def  skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I enjoy sports")

c=Child()
c.skills()
###################outside class###############
Father.skills(c)
Mother.skills(c)