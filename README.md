# amdocs_python
Daily content and assignment
a=b=c=45.78
print(a)
print(b)
print(c)
print(type(a))
print(id(a))
print(id(b))
print(id(c))
##########################################
a,b,c=10,10.8,"Test"
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
print(id(a))
print(id(b))
print(id(c))
#################################
#create a one value Tuple Object of UTKARSH ?
a=("UTKARSH",)
print(a)
print(id(a),type(a),len(a))
##################################
a="NISHANT"
print(a)
#Indexing
b=a[3]#H
print(b)
a=(10,10.8,"Test",(1,1.9,("hello",89)))
print(a)
b=a[3]#(1,1.9,("hello",89))
print(b)
#get the value hello from the given object a ?
m=a[-1][-1][0]#'hello'
print(m)
b=a[3][2][0]#'hello'
print(b)
######################################
a="NISHANT"
print(a)
b=a[2:len(a):2]#SAT
b=a[0:6:3]#0,3> NH
b=a[::2]#0:len(a):2> 0:7:2> 0,2,4,6> "NSAT"
print(b)
############Tuple############
a=(10,10.8,"Test",(1,1.9,("hello",89)),89,"Test")
print(a)
#slicing 
b=a[0:2]# 0,1
b=a[3:]#3:len(a):1> 
print(b)
###########################################
