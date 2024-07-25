d={'name':'Manish',('dept','other'):[["L&D"],[1,2,3]],'name':["Manish",'Rahul','SitaRama'],
   4576563447.78:'%*#%(*(sghdh$&98855JBJ8^%$)'}
print("d:- ",d)
print(id(d),type(d),len(d))
d1={"one":{"1":1,"2":2},"two":2}
print("d1:- ",d1)
print(id(d1),type(d1),len(d1))
#################update#######################
##update an existing key value >>>>>>>>>>>
d['name']='Test'
#######add new pair within the dict d #########
d['New Key']='New Value'
#########update dict d with the pairs of dict d1#########
d.update(d1)
print(d)
print(id(d),type(d),len(d))