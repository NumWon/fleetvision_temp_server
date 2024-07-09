from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/obd', methods=['POST'])
def receive_obd_data():
    data = request.json
    response_data = {
        "status": "success",
        "data": data,
        "timestamp": datetime.now().isoformat()
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
