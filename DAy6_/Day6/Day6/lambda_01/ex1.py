"""
f=lambda x=10,y=13 : x**2+y**2+x*y/3+56/y+78
print(type(f))
#X=10,Y=13
#positional arguments
g=f(10,13)
print(g)
# keyword arguments
g=f(y=13,x=10)
print(g)
g=f()
print(g)
"""
f=(lambda x=10,y=13 : x**2+y**2+x*y/3+56/y+78)()
print(f)

f=(lambda x=10,y=13 : x**2+y**2+x*y/3+56/y+78)(x=6,y=2)
print(f)

g=(lambda m: "Test" if m>=67 else "Waao")(40)
print(g)

f=(lambda x :x!=78)(45)
print(f)