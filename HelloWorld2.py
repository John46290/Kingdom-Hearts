from flask import Flask
app = Flask(__name__)

@app.route('/HE')
def Hello():
    return 'Hello, earth!'

if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")