from random import (randint, random, uniform, randrange, 
                    choice,sample, shuffle)

a=randint(10,90)
print(a)


b=random()
print(b)

c=uniform(-89.89,-100.89)
print(c)
d=randrange(10,22,4)
print(d)

f=("Naresh",'Suresh',"Dongli","Zu Sang",'PR01')
g=choice(f)
print(g)

h=(1,2,3,4,5)
m=sample(h,3)#list_random_samples=sample(iter_object,no_of_samples)
print(m)

k=[1,2,3,4,5]
print(k,id(k))
shuffle(k)
print(k,id(k))