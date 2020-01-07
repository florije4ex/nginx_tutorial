#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created by florije4ex / florije4ex@gmail.com at 2020/1/7.
Copyright to BIXIN GLOBAL Co.,Ltd.
"""

from flask import Flask, request

app = Flask(__name__)


@app.before_request
def before_request_func():
    print(request.url)
    print("before_request is running!")


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/name')
def name():
    return "Name: Jack!"


@app.route('/cp')
def cp():
    return "It's cp!"


if __name__ == '__main__':
    app.run(debug=True, port='8080')
