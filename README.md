# CostumeQuoterFlask

Same API like the other ones I'm making but this one using Python, Flask and MongoDB for testing purposes.

## Install requirements

pip install -r flask-pymongo pymongo flask

## Run

python ./crud.py

## API

### **getMaterials**

Returns all Materials from collection Materials

- **URL**

  /material

- **Method:**

  `GET`

### **createMaterial**

Create new material based on JSON request

- **URL**

  /material

- **Method:**

  `POST`

### **getMaterialByObjectId**

Returns one Material by ObjectId

- **URL**

  /material/<id>

- **Method:**

  `GET`
