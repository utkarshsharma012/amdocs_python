from random import randint 
for i in range(20):
    print(f"{i+1}. ",end='')
    value_1=randint(0,100)
    if (value_1>60)and(value_1<10) :
        if value_1>43:
            print(f"The Value {value_1} is Large!")
        elif 35<value_1<=43:
            print(f"The Value {value_1} is Medium!")
        else:
            print(f"The Value {value_1} is small!")
            
    else:
        print(f"The Value {value_1} is Out of Range!")
    

