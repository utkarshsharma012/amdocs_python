# non-default argument+default argument
def details(fname="sun",lname="Teena",age=21):
    name=fname+' '+lname 
    return name,age

#positional argument+keyword argument
v=details('Manish',age=89,lname='Sharma')
print(v)

v1=details()
print(v1)





