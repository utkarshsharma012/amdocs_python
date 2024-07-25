d={'name':'Manish',('dept','other'):[["L&D"],[1,2,3]],'name':["Manish",'Rahul','SitaRama'],
   4576563447.78:'%*#%(*(sghdh$&98855JBJ8^%$)'}
print(d)
print(id(d),type(d),len(d))
#######Retrieve The Values from The Dict Using Keys###############
# value_1=d['name1']# value=dict_obj[key]
# value_1=d.get('name','Key Not found!')
# print(value_1)
# for i in d: # keys
#     print(i,'===',d[i])
g=d.items()#d.keys()#d.values() #[(key1,value1),(key2,value2),(key3,value3)]
print(g)
print(type(g))
values=[]
keys=[]
for key,value in g:
    values.append(value)
    keys.append(key)
  
      
print("The Values List:-",values)
print("THe List of Keys:-",keys)
print("Back 2 Dict:-",dict(zip(keys,values)))









