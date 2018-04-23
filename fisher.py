"""
Created by Allen on '2018/4/18 14:40'
"""
from flask import Flask
__author__ = 'Allen'

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello word'


app.run(debug=True)


