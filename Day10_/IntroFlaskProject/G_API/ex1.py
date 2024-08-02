import  requests as req
url="http://127.0.0.1:5000/stores"
url="http://127.0.0.1:5000/stores/Jio Store"
response=req.get(url)
if response.status_code==200:
    print(response.text)
