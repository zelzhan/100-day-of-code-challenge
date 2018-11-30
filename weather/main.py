#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query
from pprint import pprint as pp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Astana'}, {'name':'Almaty'}])


@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)
    
if __name__=='__main__':
    app.run(debug=True)