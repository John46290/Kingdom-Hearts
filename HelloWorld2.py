from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/HE', methods=['GET'])
def Hello():
    name = request.form.get('myvar1', False)
    output = render_template("hello2.html")
    return output

if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")