#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query
from pprint import pprint as pp
from search import Search
from helpers import extract_day, jsonProcess
import time
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

session = []


@app.route('/', methods=['GET', 'POST'])
def index():
    print("first")
    form = Search()
    if form.validate_on_submit():
        time = session.pop()
        time = extract_day(time)                   #extract day, month and year as dictionary
        city = request.form.get('city')
        data = query(city, time)
        print(data)
        return redirect(url_for('result', data = data, city = city))

    return render_template('search.html', form = form)

@app.route("/result")
def result():
    data = request.args.getlist('data')        #max and min temps, comes from the index page and passed as a parameter for render template 
    data = jsonProcess(data)
    print("My data", data)
    return render_template('results.html', data=data)

@app.route("/getTime", methods=['GET'])
def getTime():
    print("second")
    session.append(request.args.get("time"))
    print(session[0])
    return "Done"


    
if __name__=='__main__':
    app.run(debug=True)