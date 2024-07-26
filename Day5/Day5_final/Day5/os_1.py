import os 
print(os.getcwd())
print(os.listdir())
path=r'C:\Users\OM\eclipse-workspace\01_22July_AmDocs\Day5\files'
print(path)
path1=os.path.join(os.getcwd(),'files')
print(path1)
os.chdir(path1)
print("After Change Dir")
print(os.getcwd())
print(os.listdir())

with open('lines.txt','r') as fh:
    for line in fh:
        print(line.strip())
    print("Done")
