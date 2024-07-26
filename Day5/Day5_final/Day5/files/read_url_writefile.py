#python -m pip install requests
import requests  
url=r"https://github.com/xpn/CUDA-MD5-Crack/raw/master/wordlist.txt"
res=requests.get(url)
print(res)
print(res.status_code)
if res.status_code==200:
#     print(res.content)
#     print(res.text)
    out=open('web1.txt','wb')
    out.write(res.content)
    out.close()
    print("Done")
    
else:
    print(f"Invalid Response {res}")