from flask import Flask, render_template
app = Flask(__name__)

@app.route('/HW')
def Hello():
    output = render_template('hello.html')
    return output

if __name__ == '__main__':
    app.run(port=8080, debug=True, host="0.0.0.0")