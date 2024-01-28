from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
cors = CORS(app)


@app.route('/button_press', methods=['POST'])
def handle_button_press():
    data = request.json  # Assuming JSON data is sent in the request body
    # Call the handler function with the data received from the frontend
    response = handler(data)
    return jsonify(response)

def handler(data):
    # Your handler logic here
    # Process the data received from the frontend
    print("Button pressed with data:", data)
    return {'message': 'Button press handled successfully'}

if __name__ == "__main__":

    app.run(host="localhost", port=5000, debug=True)
