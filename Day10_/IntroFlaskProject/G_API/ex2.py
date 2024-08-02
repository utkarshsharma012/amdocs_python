import  requests as req
# url="http://127.0.0.1:5000/stores"
# data={'name':"Test Store"}
url="http://127.0.0.1:5000/stores/Jio Store/item"
data={'name':"Jio Mobile 5G","price":67.89}
response=req.post(url,json=data)
if response.status_code==200:
    print(response.text)
else:
    print(response.status_code)
