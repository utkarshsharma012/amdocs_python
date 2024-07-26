fh=open('lines.txt','r')
out=open('out.txt','w')

for line in fh:
    if line.strip().endswith('.mp3')  or line.__contains__('hero'):
        print(line.strip(),file=out)
    
print("Done")
fh.close()
out.close()
# hero
#.mp3
