import sys 
path1=r"C:\Users\OM\eclipse-workspace\01_22July_AmDocs\Day5\module_1\case2\bin\sys"
sys.path.append(path1)

from dongli_1 import odd_even,Area
from time import sleep
 
print("===========================calling_1.py File is executed=========")
f=odd_even('8')
print(f)
sleep(3)
a=Area()
print(a)