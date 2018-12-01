#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query
from pprint import pprint as pp
from search import Search
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
 
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Search()
    if form.validate_on_submit():
        city = request.form.get('city')
        data = query(city)
        return redirect(url_for('result', data = data, city = city))

    return render_template('search.html', form = form)

@app.route("/result")
def result():
    data = request.args.getlist('data')[0] #max and min temps, comes from the index page and passed as a parameter for render template    
    data = data.replace("\'", "\"")
    data = json.loads(data)
    return render_template('results.html', data=data)

    
if __name__=='__main__':
    app.run(debug=True)