import pymongo
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://hider:12345@cluster0.v3veas6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/FANBOOK", methods=["POST"])
def FANBOOK_post():
    name_receive = request.form['name']     
    comment_receive = request.form['comment']
    doc = {
        'name': name_receive,           
        'comment': comment_receive
    }
    db.FANBOOKS.insert_one(doc)
    return jsonify({'msg': 'POST request!'})

@app.route("/FANBOOK", methods=["GET"])
def FANBOOK_get():
    FANBOOK_list = list(db.FANBOOKS.find({}, {'_id': False}))
    return jsonify({'FANBOOKS': FANBOOK_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
