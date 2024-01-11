from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {
        'id': 1,
        'name': 'Sample Data',
        'value': 42
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
