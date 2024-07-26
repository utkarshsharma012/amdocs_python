"""
This is User define modules with functions 
1.Area
2.Odd_even

"""


def Area():
#     global option
    from math import sqrt,pi
    print('''Shapes:
        1.Triangle
        2.Rectangle
        3.Circle
        4.Square''')
    list1=['Triangle','Rectangle','Circle','Square']
    option = input('Enter you choice: ')
    if type(option)==str:
        if option.isdigit():
            option=int(option)
        else:
            option=option
    choice='None'
    if type(option)==type(67):
        if option<=len(list1) :
            choice=list1[option-1]
    elif type(option)==type(67.90):
        pass
    elif option.lower() in [n.lower() for n in list1]:
        choice =option
       
    if option == 1 or choice.lower()=='triangle' :
        a,b,c = eval(input('Enter 3 sides of triangle: '))
        s = (a+b+c)/2
        area=sqrt(s*(s-a)*(s-b)*(s-c))
        #print('The area of triangle is',area)
    elif option == 2 or choice.lower()=='rectangle':
        a,b = eval(input('Enter 2 sides of rectangle: '))
        area =a*b
        #print('The area of rectangle is',area)
    elif option == 3 or choice.lower()=='circle':
        r = eval(input('Enter radius of circle: '))
        area =  pi * r**2
        #print('The area of circle is',area)
    elif option == 4 or choice.lower()=='square':
        a = eval(input('Enter side of square: '))
        area = a*a
        #print('The area of square is',area)
    else:
        print('Invalid option!!!')
        choice=None
        area=None
        
    return choice,area

def odd_even(number='5'):
    if type(number)==str:
        if number.isdigit():
            number = int(number)
            from math import factorial   
            if (number % 2) == 1:
                str1 = "Odd"
                fact = factorial(number)
            else:
                str1 = "Even"
                fact = factorial(number)  
            return number, str1, fact  
        else:
            str1=None
            fact=None
            print("Data Type:-",type(number),'Is Invalid!..')
            return number, str1, fact
    else:
        str1=None
        fact=None
        print("Data Type:-",type(number),'Is Invalid!')
        return number, str1, fact

if __name__=="__main__":
    from time import sleep
    print('===========================dongli_1.py File is executed======================================')
    out1=Area()
    print(f'The area of {out1[0]} is {out1[1]}')
    print('==================================')
             
    sleep(4)
                    
    a = input("Enter a number: ")
    num,out,fact1 = odd_even(a)                        
    print(f'The value {num} is {out} and factorial is {fact1}.')
        #       
        #           
    print('===================================================================')

