class demo:
    var=90
    def gold(self,fname,age=56):
        print('This is glod method!')
        name=fname+' '+'Sharma'
        return age,name#{'age':age,'fname':fname}#[age,name]
        
############################################################        
obj1=demo()
print(obj1)
print(obj1.var)
#calling of the method
v=obj1.gold('Manish',67)
print(v)
############################################
obj2=demo()
h=obj2.gold(age=34, fname='Raj')
print(h)