d={'name':'Manish',('dept','other'):[["L&D"],[1,2,3]],'name':["Manish",'Rahul','SitaRama'],
   4576563447.78:'%*#%(*(sghdh$&98855JBJ8^%$)'}
print("d:- ",d)
print(id(d),type(d),len(d))
d1={"one":{"1":1,"2":2},"two":2}
print("d1:- ",d1)
print(id(d1),type(d1),len(d1))
############create dict d3 with the pairs of dict d and d1 ?##############
######Note:- without any change in d and d1####################
#######3 lines#########
# d3={}
# d3.update(d)
# d3.update(d1)
######2 Lines#########
# d3=d.copy()
# d3.update(d1)
#####1 lines ###########################
d3={**d,**d1}

print("d3:- ",d3)
print(id(d3),type(d3),len(d3))


print(d3 is d)#F
print(d3 is d1)#F