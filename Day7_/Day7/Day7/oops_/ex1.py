class demo:
    print('This is demo class')
    var=90#public
    
print(demo.var )   #90# get the value from the class demo memory
#create the object of the class
obj1=demo()
print(obj1)
print(obj1.var)#90
obj1.var+=10 # update the value of var within obj1 memory 
print(demo.var)#90
print(obj1.var)#100

obj2=demo() # new object
print(obj2.var)#90
print(id(obj1),id(obj1.var))
print(id(obj2),id(obj2.var))
