from flask import Flask
from flask import request
from flask import jsonify
from bson.json_util import dumps
import json
import dbConnect
app = Flask(__name__)

@app.route("/insert", methods = ['POST'])
def insert_data():
    try:
        data=request.get_json()
        dbConnect.db.employee.insert_one(data)
        return jsonify({'message' : 'successfully entered data'})
    except Exception as e:
        return jsonify({'error' : str(e)})


@app.route("/search", methods = ['POST'])
def get_search_data():
    try:
        data=request.get_json(force=True)
        result=dbConnect.db.employee.find(data)
        list_result=[]
        for row in result:
            list_result.append(row)
        return dumps(list_result)
    except Exception as e:
        return jsonify({'error':str(e)})

@app.route("/")
def hello():
    return "Hello World!"
if __name__ == '__main__':
    app.run(debug=True)