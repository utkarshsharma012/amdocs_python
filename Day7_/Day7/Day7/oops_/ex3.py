class demo:
    var=90
    def gold(self,fname,age=56):
        print('This is glod method!')
        name=fname+' '+'Sharma'
        self.var+=10# update the value within the object memory of data var
        return age,name,self.var#(get and return the value from the its object memory)
#         return age,name,demo.var#(get and return the value from the its class memory)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
############################################################        
obj1=demo()
#calling of the method
v=obj1.gold('Manish',67)
print(v)
############################################
obj2=demo()
h=obj2.gold(age=34, fname='Raj')
print(h)