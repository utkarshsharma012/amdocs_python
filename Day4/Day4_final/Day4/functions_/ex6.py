def details(fname,lname,age,*marks,**subjects): #*args > tuple , #**kwargs > dict
    name=fname+' '+lname 
    return name,age,marks,subjects



v1=details('Raj','Meena',56,89,78,67,89,math=67,arts=90,science=78)
print(v1)