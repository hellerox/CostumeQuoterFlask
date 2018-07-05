from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'ACdev'
app.config['MONGO_URI'] = 'mongodb+srv://'

mongo = PyMongo(app)

@app.route('/material', methods=['GET'])
def get_all_materials():
  materials = mongo.db.materials
  output = []
  for m in materials.find():
    print(materials.count())
    print("out",m)
    output.append({'id':str(m['_id']),'nombrematerial': m['nombrematerial'], 'idtipomaterial': m['idtipomaterial'],'idmedidamaterial':m['idmedidamaterial'],'costo':m['costo']})
  return jsonify(output)

@app.route('/material/<string:id>', methods=['GET'])
def get_one_material(id):
  material = mongo.db.materials
  m = material.find_one({"_id": ObjectId(id)})
  print("out",m)
  if m:
    output ={'id':id,'nombrematerial': m['nombrematerial'], 'idtipomaterial': m['idtipomaterial'],'idmedidamaterial':m['idmedidamaterial'],'costo':m['costo']}
  else:
    output = "No such name"
  return jsonify(output)

@app.route('/material', methods=['POST'])
def add_material():
  material = mongo.db.materials
  nombrematerial = request.json['nombrematerial']
  idtipomaterial = request.json['idtipomaterial']
  idmedidamaterial = request.json['idmedidamaterial']
  costo = request.json['costo']
  objectid = material.insert({'nombrematerial': nombrematerial, 'idtipomaterial': idtipomaterial,'idmedidamaterial':idmedidamaterial,'costo':costo})
  print(objectid)
  return jsonify({'id' : str(objectid)})

if __name__ == '__main__':
    app.run(debug=True)