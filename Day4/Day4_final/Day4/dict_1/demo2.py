a=(1,2,3,4)
b=[5,6,"Test",8]
#create a list c with the  values of  tuple a and list b >  c=[1,2,3,4,5,6,7,8] in one line without using + .
# c=a.copy()# if a is list
# c.extend(b)
c=[*a,*b] # *args > arrays
print(c)
print(c is a)
print(c is b)
print(id(a))
print(id(a[0]))

d={'name':'Manish',('dept','other'):[["L&D"],[1,2,3]],'name':["Manish",'Rahul','SitaRama'],
   4576563447.78:'%*#%(*(sghdh$&98855JBJ8^%$)'}
d1={"one":{"1":1,"2":2},"two":2}


d3={**d,**d1}# **Kwargs > dict
print(d3)
print(type(d3))