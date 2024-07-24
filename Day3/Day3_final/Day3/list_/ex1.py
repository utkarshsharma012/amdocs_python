a=[]
a=['Hello']
a=[1,1.2,"Hello",(78,"Test"),[90,78]]
print(a)
print(id(a),type(a),len(a))
########indexing######
b=a[2]#"Hello"
print(b)
#######slicing###########
b=a[0::2]#0:5:2 > 0,2,4> [1,"Hello",[90,78]]
print(b)
########################
for i in a:
    print(i)
######################
g=a.index('Hello')
print(g)