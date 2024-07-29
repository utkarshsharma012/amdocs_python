# create a list of 1000 random integer numbers ?
from random import randint
list_r=[]
for i in range(1000):
    list_r.append(randint(10,67))
    
print(list_r)
#list comprehension in python    
# [value for loop_var in iterObject]  
# list_r=[randint(10,67) for n in range(1000)] 
# print(list_r)
# [value for loop_var in iterObject if exp] 
# a=[n for n in range(50) if n%2!=0]
# print(a)
# # [value for loop_var in iterObject if exp1 if exp2] 
# a=[n for n in range(50) if n%2!=0 if n%5==0]
# print(a)
# 
# # [value if exp else value2 for loop_var in iterObject ] 
# a=[n if n%2!=0 else None for n in range(1,20) ]
# print(a)
# number's > 0-9
h='9' not in [str(n) for n in range(10)]
print(h)















 