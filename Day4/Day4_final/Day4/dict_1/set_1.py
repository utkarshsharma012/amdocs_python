# g=[1,1.2,(67,89),"Hello",90,90,90,"Hello",1,1.2]
# print(g)
# print(len(g),type(g))
# a=set(g)
a={1, 1.2, (67, 89), 'Hello', 90}
print(a)
print(id(a),type(a),len(a))
a.add("Test")
a.discard("Hello")
print(a)
print(id(a),type(a),len(a))
###############################
for i in a:
    print(i)