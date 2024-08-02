from flask import Flask,jsonify,request
app = Flask(__name__)#WSGI App object
#END Points
#GET :- used to send data back to the client
#Post :- used to receive data
stores=[{'name':"Jio Store",'items':[{'name':"jio cable",'price':15.99}]},
{'name':"Airtel Store",'items':[{'name':"Airtel 5g Sim",'price':0.91}]}]
#get the stores data at client side as json response
#http://127.0.0.1:5000/stores
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})

#http://127.0.0.1:5000/stores
@app.route('/stores',methods=['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
    'name':request_data['name'],
    'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)
#http://127.0.0.1:5000/stores/Store_name #Get
@app.route('/stores/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message': 'Store not found!'})

#Add Items Into the stores.?
#POST
@app.route('/stores/<string:name>/item',methods=['POST'])
def create_item(name):
    response_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={'name':response_data['name'],
            'price':response_data['price']}
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':"Store not found!"})

#Get Item From the store.?
#Get
@app.route('/stores/<string:name>/item')
def get_item(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'Store not found!'})







if __name__ == '__main__':
    app.run(debug=True)
