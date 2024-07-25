def details(fname,lname,age):
    name=fname+' '+lname 
    return name,age

#positional argument+keyword argument
v=details('Manish',age=89,lname='Sharma')
print(v)

v1=details('Raj','Meena',age=56)
print(v1)




"""
print('Manish',"Sharma",sep='===',end=' ')
print("Hello")


print('Manish',"Sharma",end=' ',sep='===')
print("Hello")


print(end=' ','Manish',"Sharma",sep='===')#Error 
print("Hello")
"""
