class demo:
    var=90
    name=None
    def gold(self,fname,age=56):
        print('This is glod method!')
        name=fname+' '+'Sharma' 
        self.name=name
        return age,name,self.var

    def out(self,fname,dept):
        self.gold(fname=fname, age=56)# calling a method inside another method
        name1=self.name.split(' ')[0]+' Meena' 
        return name1  ,dept 
            
        
       
        
        
        
############################################################        
obj1=demo()
#calling of the method
m=obj1.out('Manish','L&D')
print(m)
############################################
obj2=demo()
m1=obj2.out("Raj","IT")
print(m1)
####################
obj3=demo()
print(obj3.name)