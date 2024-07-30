class demo:
    var=90
    name=None
    def gold(self,fname,age=56):
        print('This is glod method!')
        name=fname+' '+'Sharma' #local
        #create an attribute name
        self.name=name # create an attribute at object level
#         demo.name=name # create an attribute at class level
        return age,name,self.var

    def out(self):
        name1=self.name.split(' ')[0]+' Meena' 
        return name1   
            
        
       
        
        
        
############################################################        
obj1=demo()
#calling of the method
v=obj1.gold('Manish',67)
print(v)
m=obj1.out()
print(m)
############################################
obj2=demo()
h=obj2.gold(age=34, fname='Raj')
print(h)
m1=obj2.out()
print(m1)
####################
obj3=demo()
print(obj3.name)