try:
    fh=open('lines.txt','r')
    for line in fh:
        print(line.strip())
    d=1/0
except IOError as o:
    print("Error Name:-",o.__class__.__name__)
    print("Error Msg:-",o)
    with open('out.txt') as fg:
        print(fg)
    fg.close()
except Exception as e:
    print("Error Solved!")
    print("Error Name:-",e.__class__.__name__)
    print("Error Msg:-",e)
    
    
print("==============")
import datetime as dt 
now=dt.datetime.now()
print(now)