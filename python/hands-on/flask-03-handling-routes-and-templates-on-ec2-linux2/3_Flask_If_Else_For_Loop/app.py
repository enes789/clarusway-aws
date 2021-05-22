from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first = "This is my first conditions"
    return render_template('index.html', message = first)

@app.route('/enes')
def eren():
    name = ["Serdar", "Elnur", "Mehmet", "Ahmet"]
    return render_template('body.html', object = name, developer_name = "Enes")




if(__name__) == '__main__':
    app.run(debug=True)