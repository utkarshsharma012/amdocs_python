# seq1=[67,24,56,89,78,45,90,92,89]
# f=list(filter((lambda x: x%2!=0),seq1))
# print(f)
# str1="I122N33D343I33@333     D454E34r3L444H67734I"
# print(str1)
# # f=''.join(filter(lambda x : not x.isdigit(),str1))
# f=''.join(filter(lambda x : x not in [str(n) for n in range(10)],str1))
# print(f)

sq=[1,2,3,4,5]
g=list(map(lambda x : x+3,sq))
print(g)

seq=[n*34.6 for n in range(1,17)]
print(seq)

g=0
for i in seq:
    g=g+i 
    
print(g)

from functools import reduce 
g=reduce(lambda x,y: x+y, seq)
print(g)
 












