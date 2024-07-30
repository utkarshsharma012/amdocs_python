#Multiple Inheritance
class Father:
    def gardening(self):
        print("I enjoy gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

class Child(Mother,Father):
    def  skills(self):
        print("I enjoy sports")

c=Child()
c.skills()
c.gardening()
c.cooking()