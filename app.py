from flask import  Flask, jsonify , render_template , request
from bson.objectid import ObjectId
import json
import pymongo

app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["restaurantDB"]
mycol = mydb["orders"]

orders = [{"id":1,"name":"ผัดกระเพรา"},{"id":2,"name":"ต้มยำกุ้ง"},{"id":3,"name":"ผัดไทย"},{"id":4,"name":"ลาบเป็ด"}]



@app.route("/")
def index():
    texts = "Hello CodingByamp"
    return texts



@app.route("/api/getorder")
def getorder():
    output = []
    for x in mycol.find():
        output.append({'_id':str(x['_id']),'name': x['name']})
    return jsonify(output)
       

@app.route("/page/order")
def vieworder():
    return render_template("order.html")


@app.route("/api/insertorder", methods =['POST'])
def isertOrder():
    if not request.json or not 'name' in request.json:
       return 400
    order = {"name": request.json['name']}

    #orders.append(order)
    x = mycol.insert_one(order)
    return jsonify({'status':'success'})


@app.route("/api/deleteorder", methods= ['POST'])
def isdelete():
    if not request.json or not 'id' in request.json:
        return 400
    obj = {"_id" : ObjectId(request.json['id'])}
    x = mycol.delete_one(obj)
   # print(x)
    return jsonify({'status':'success'})



if __name__ == "__main__":
    app.run(debug=True)