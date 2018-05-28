"""
Created by Allen on '2018/4/18 14:40'
"""
import json
from flask import Flask


__author__ = 'Allen'


app = Flask(__name__)
app.config.from_object("config")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=81)


