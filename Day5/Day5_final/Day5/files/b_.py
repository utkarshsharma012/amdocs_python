fh=open('bigfile.txt','r')
out=open('out.txt','w')

for line in fh:
        print(line.strip(),file=out)
    
print("Done")
fh.close()
out.close()
# hero
#.mp3
