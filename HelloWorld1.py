from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/hello.html', methods=['GET'])
def Hello():
    output = render_template("hello.html")
    return output

@app.route('/hello2.html', methods=['GET'])
def Hi():
    variable = request.args.get('myvar1')
    output = render_template("hello2.html", variable=variable)
    return output

if __name__ == '__main__':
    app.run(port=8080, debug=True, host="0.0.0.0")