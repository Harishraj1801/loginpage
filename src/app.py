from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    target = request.form['target']
    features = request.form['features']
    time_period = request.form['timePeriod']

    # Save the file to the MongoDB server
    mongo.save_file(file.filename, file)
    
    # Save the file metadata to the MongoDB server
    mongo.db.files.insert_one({
        'filename': file.filename,
        'target': target,
        'features': features,
        'time_period': time_period
    })
    
    return {'message': 'File uploaded successfully'}

if __name__ == '__main__':
    app.run(debug=True)
