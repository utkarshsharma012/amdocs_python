class details:
    def __init__(self,name,age,dept):
        self.name=name #public
        self.__age=age #private
        self._dept=dept#protected 
        print(self.__age)
        
        
obj=details('Manish',34,"L&D")
print(obj.name)
obj.name="Raj"
print(obj.name)

print(obj.__age)
