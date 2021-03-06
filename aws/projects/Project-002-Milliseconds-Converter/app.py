from flask import Flask, render_template, request

app = Flask(__name__)

def convert(milliseconds):
    hour_in_milliseconds = 60*60*1000
    hours = milliseconds // hour_in_milliseconds 
    milliseconds_left = milliseconds % hour_in_milliseconds 
    minutes_in_milliseconds = 60*1000
    minutes = milliseconds_left // minutes_in_milliseconds 
    milliseconds_left %= minutes_in_milliseconds
    seconds = milliseconds_left // 1000
     
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)

@app.route('/', methods = ['GET'])
def main_get():
    return render_template('index.html', developer_name = 'Enes', not_valid = False)

@app.route('/', methods = ['POST'])
def main_post():
    alpha = request.form['number']  
    if not alpha.isdecimal():
       return render_template('index.html', developer_name = 'Enes', not_valid = True) 

    number = int(alpha)
    if number < 1:
        return render_template('index.html', developer_name = 'Enes', not_valid = True)

    return render_template('result.html', developer_name = 'Enes', milliseconds = number, result = convert(number))


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)