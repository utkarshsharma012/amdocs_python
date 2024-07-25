def details(fname,lname,age):
    name=fname+' '+lname 
    return name,age

#keyword argument
v=details(lname='Sharma',fname='Manish',age=89)
print(v)

v1=details(age=56,fname='Raj',lname='Meena')
print(v1)