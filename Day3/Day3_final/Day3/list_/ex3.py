a=[1,1.2,"Hello",(78,"Test"),[90,78]]
print(a)
print(id(a),type(a),len(a))
##########delete value from the List#########
# #using index Number 
# del a[2]
# #Using Value
# a.remove(1.2)
# m=a.pop() # delete the last value from the list and return the deleted Value
m=a.pop(3) # delete the 3rd index no value from the list and return the deleted Value
print("Deleted Value:-",m)
print(a)
print(id(a),type(a),len(a))