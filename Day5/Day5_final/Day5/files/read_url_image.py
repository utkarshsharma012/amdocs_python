#python -m pip install requests
import requests  
url=r"http://craphound.com/images/1006884_2adf8fc7.jpg"
res=requests.get(url)
print(res)
print(res.status_code)
if res.status_code==200:
#     print(res.content)
#     print(res.text)
    out=open('image_wb.jpeg','wb')
    out.write(res.content)
    out.close()
    print("Done")
    
else:
    print(f"Invalid Response {res}")