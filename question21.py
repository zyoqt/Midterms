from flask import Flask, jsonify, request
app = Flask(__name__)
hearts = [
    {
        "heart_id": "1",
        "date": "2023-12-15",
        "heart_rate": 75
    },
    {
        "heart_id": "2",
        "date": "2023-12-15",
        "heart_rate": 88
    }
]

@app.route('/hearts', methods=['GET'])
def gethearts():
    return jsonify(hearts)

@app.route('/hearts', methods=['POST'])
def add_heart():
    heart = request.get_json()
    hearts.append(heart)
    return {'heart_id': len(hearts)}, 200

@app.route('/hearts/<int:index>', methods=['GET'])
def get_heart(index):
    for heart in hearts:
        if heart['heart_id'] == str(index):
            return jsonify(heart)

@app.route('/hearts/<int:index>', methods=['PUT'])
def update_heart(index):
    data = request.get_json()
    for heart in hearts:
        if heart['heart_id'] == str(index):
            heart['date'] = data.get('date', heart['date'])
            heart['heart_rate'] = data.get('heart_rate', heart['heart_rate'])
            return 'Heart record updated successfully', 200

@app.route('/hearts/<int:index>', methods=['DELETE'])
def delete_heart(index):
    for i, heart in enumerate(hearts):
        if heart['heart_id'] == str(index):
            hearts.pop(i)
            return 'The heart has been deleted', 200

if __name__=='__main__':
    app.run()
