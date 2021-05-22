from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World"

@app.route('/enes')
def second():
    return "This is Enes's page"

@app.route('/third/subthird')
def third():
    return "This is the third page."


@app.route("/forth/<string:id>")
def forth(id):
    return f"Id of thid page is {id}"

if __name__=='__main__':
    app.run(debug = True)