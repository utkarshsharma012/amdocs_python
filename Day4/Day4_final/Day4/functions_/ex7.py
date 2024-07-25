# non-default argument+default argument
def details(fname="sun",lname="Teena",age=21):
    global name
    name=fname+' '+lname # func variable scope > local
    out="Copy1" # func variable scope > local , func always give preference to their local variable over any global vaiable.
    return name,age,out

out="Book" # Script Variable Scope > Global
#positional argument+keyword argument
v=details('Manish',age=89,lname='Sharma')
print(v)#Copy1
print(out)#Book
print(name)