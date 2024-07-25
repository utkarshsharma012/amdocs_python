d={'name':'Manish',('dept','other'):[["L&D"],[1,2,3]],'name':["Manish",'Rahul','SitaRama'],
   4576563447.78:'%*#%(*(sghdh$&98855JBJ8^%$)'}
print("d:- ",d)
print(id(d),type(d),len(d))
#############delete####################
# del d['name']
# d.pop('name1',None)

#######update an existing key name > NewName ?
#output :- {('dept', 'other'): [['L&D'], [1, 2, 3]], 4576563447.78: '%*#%(*(sghdh$&98855JBJ8^%$)','NewName': ['Manish', 'Rahul', 'SitaRama']}
# d['NewName']=d['name']
# del d['name']
d['NewName']=d.pop('name')


print("d:- ",d)
print(id(d),type(d),len(d))