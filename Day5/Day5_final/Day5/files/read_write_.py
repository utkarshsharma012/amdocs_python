fh=open('bigfile.txt','rb')
out=open('out_bytes.txt','wb')
buffersize=50000#bytes 
buffer=fh.read(buffersize)

while buffer:
    out.write(buffer)
    buffer=fh.read(buffersize)
    print(".")
    

print("Done")
fh.close()
out.close()