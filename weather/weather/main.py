from Flask import Flask, flash, render_template, redirect, request, url_for
from pprint import pprint as pp
from weather import query

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Toronto'}, {'name':'Montreal'}, {'name':'Calgary'},
        {'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},
        {'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'}, 
        {'name':'Quebec'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    response = query(select)
    pp(response)
    if response:
       data.append(response)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)

if __name__=='__main__':
    app.run(debug=True)

