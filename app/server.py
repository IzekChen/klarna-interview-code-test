import sys
from flask import Flask, request,render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tasks/fibonacci")
def fibo():
    return render_template('fibonacci.html')

@app.route("/tasks/factorial")
def fac():
    return render_template('factorial.html')

@app.route("/tasks/ackermann")
def ack():
    return render_template('ackermann.html')

@app.route("/result/fabonacci", methods=['POST'])
def sum_of_fabonacci():
    
    def sum_helper(n):
        pre, cur = 1, 1
        for i in range(n-1):
            pre, cur = cur, cur+pre
        return pre

    number = int(request.form['fibonacci'])
    
    if number == 0:
        return render_template("result.html",result = '0' , task = 'Sum of fibonacci', number = number, route='fibonacci')
    elif number == 1:
        return render_template("result.html",result = '1' , task = 'Sum of fibonacci', number = number, route='fibonacci')
    elif number > 1000:
        return render_template("result.html",result = 'you input is higher than 1000' , task = 'Sum of fibonacci', number = number, route='fibonacci')
    res = str(sum_helper(number))
    return render_template("result.html",result = res , task = 'Sum of fibonacci', number = number, route='fibonacci')

@app.route("/result/factorial", methods=['Post'])
def cal_factorial():

    def sum_helper(n):
        if n < 0:
            return "the input number required a non-negative number"
        elif n == 0:
            return 1
        else:
            return n * sum_helper(n-1)

    number = int(request.form['factorial'])
    res = str(sum_helper(number))
    return render_template("result.html", result=res, task = 'The factorial', number = number, route='factorial')
    #return res

@app.route("/result/ackermann", methods=['Post'])
def ackermann():

    def helper(m, n ):
        if m == 0:
            return n+1
        elif n == 0:
            return helper(m-1, 1)
        else:
            return helper(m-1, helper(m,n-1))

    m, n  = int(request.form['Ackermann_m']), int(request.form['Ackermann_n'])
    if (( m < 0 ) and ( n < 0 )):
        return render_template("result.html", result="only positive numbers are allowed for both field", task = 'The ackermann', number = "A({}, {})".format(m,n ), route='ackermann')
    res = helper(m, n)
    #print(res)
    #return str(res)
    return render_template("result.html", result=str(res), task = 'The ackermann', number = "A({}, {})".format(m,n ), route='ackermann')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)