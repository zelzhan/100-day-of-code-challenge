#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query
from pprint import pprint as pp
from search import Search

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
 
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Search()
    if form.validate_on_submit():
        city = request.form.get('city')
        temps = query(city)
        return redirect(url_for('result', temps = temps))

    return render_template('search.html', form = form)




@app.route("/result")
def result():
    temps = request.args['temps'] #max and min temps, comes from the index page and passed as a parameter for render template    
    return render_template('results.html', temps = temps)





# @app.route("/result" , methods=['GET', 'POST'])
# def result():
#     data = []
#     error = None
#     select = request.form.get('comp_select')
#     pp(select)
#     resp = query(select)
#     pp(resp)
#     if resp:
#        data.append(resp)
#     if len(data) != 2:
#         error = 'Bad Response from Weather API'
#     return render_template(
#         'result.html',
#         data=data,
#         error=error)



    
if __name__=='__main__':
    app.run(debug=True)