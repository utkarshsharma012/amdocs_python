"""
file_object=open('filename','mode')
Modes:
r> read
w> write 
r+> read/write 
a> append 
x> create new file 
######
rb > read binary file 
##################
"""
fh=open("lines.txt",'r')
print(fh)
for line in fh:
    print(line.strip())

print("==")
fh.seek(0)
# one_line=fh.readline()
list_lines=fh.readlines()
print(list_lines)

fh.close()

# fh.readline() #Error 







