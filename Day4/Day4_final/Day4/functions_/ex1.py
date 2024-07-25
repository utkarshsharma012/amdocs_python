def demo():
    print("This is demo function")
    dept="L&D"
    age=67
    dept12=["L&D"]
    return age,dept #{'dept':dept,"age":age}#[age,dept]
    
    
m=demo(78)#calling of the function.
print(m,type(m))
if type(m)==tuple or type(m)==list:
    #indexing 
    dept=m[1]
    print("Dept:-",dept)
elif type(m)==dict:
    #keys
    dept=m['dept']
    print("Dept:-",dept)