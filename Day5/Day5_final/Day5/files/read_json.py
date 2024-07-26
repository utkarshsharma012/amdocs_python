import json 
#read_json > dict
fh=open('data.json','r')
print(fh)
json_dict=json.load(fh)
print(json_dict)
print(type(json_dict))
print(json_dict['students'][0]['name'])
#################################
# dict> json data 
with open('python_json.json','w') as file:
    dict_json=json.dumps(json_dict)
    print(dict_json)
    print(type(dict_json))
    file.write(dict_json)
    
