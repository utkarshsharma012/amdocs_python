# a="  thIs is NisHant HOuse.   "
# print(a,len(a))
# a=a.strip()#a.rstrip()#a.lstrip()
# print(a,len(a))
# b=a.replace('is', 'mm')#a.lower()#a.upper()#a.capitalize()
# print(b,len(b))
# a='123.'
# b=a.isdigit()# True : If string conatins only digits 
# print(b)
# a='Hello1'
# b=a.isalpha()# True : If string conatins only A-z chars' 
# print(b)
# a='NISHANT#24566 _'
# b=a.isupper()# True : If string contains Upper Case A_Z ' 
# print(b)

# a='nishant#24566 _'
# b=a.islower()# True : If string contains lower Case a-z ' 
# print(b)
# value="Kal Ho na ho.mp3"
# g=value.endswith('.mp3')
# print(g)
# 
# value="Kal Ho na ho.mp3"
# g=value.startswith('Kal')
# print(g)
# 
# value="Kal Ho na ho.mp3"
# g=value.__contains__('Ho')
# print(g)

name="Manish12"
age=78

out="The NAme:-"+name+" And The Age:- "+str(age)
# out=(1,2,3)+("Hello","Hii")
print(out)
#format()
out="The NAme is {} and Age is {}".format(name,age)
print(out)
out="The NAme is {1} and Age is {0}".format(name,age)
print(out)
out="The NAme is {a2} and Age is {a1}".format(a1=name,a2=age)
print(out)

#f-string 
out=f"The NAme is {name} and Age is {age}"
print(out)












