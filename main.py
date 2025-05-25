from flask import Flask, request, jsonify

app= Flask(__name__)

# in-memory datas(list of Dictionaries)
ice_creams = [
    {"id": 1, "flavor": "Vanilla", "price": 50},
    {"id": 2, "flavor": "Chocolate", "price": 60},
    {"id": 3, "flavor": "Strawberry", "price": 55}
]

#Home message
@app.route('/')
def home():
    return "Welcome"

#Get all ice creams
@app.route('/icecreams',methods=['GET'])
def get_ice_creams():
    return jsonify(ice_creams)

#Add a new Ice cream
@app.route('/icecreams',methods=['POST'])
def add_icecream():
    data=request.get_json()
    if ice_creams:
        new_id= ice_creams[-1]['id'] + 1
    else:
        new_id=1
    new_ice_cream= {
        "id": new_id,
        "flavor": data.get("flavor"),
        "price": data.get("price")
    }
    ice_creams.append(new_ice_cream)
    return jsonify(ice_creams), 201

#Update an Ice cream
@app.route('/icecreams/<int:ice_id>',methods=["PUT"])
def update_ice_cream(ice_id):
    data=request.get_json()
    for i in ice_creams:
        if i["id"] == ice_id:
            i["flavor"]= data.get("flavor",i["flavor"])  #Updates flavor and price and/or price using data.get() — keeps old value if no new value is given.
            i["price"]= data.get("price",i["price"])
            return jsonify(i)
    return jsonify({"error": "Ice cream not found"}),404  

#Delete an Ice cream 
@app.route('/icecreams/<int:ice_id>',methods=['DELETE'])
def delete_ice_cream(ice_id):
    for i in ice_creams:
        if i["id"] == ice_id:
            ice_creams.remove(i)
            return jsonify({"message": "Ice crem deleted successfully!"}),200
    return jsonify({"error": "Ice cream not found"}),404

if __name__ == '__main__':
    app.run(debug=True)
