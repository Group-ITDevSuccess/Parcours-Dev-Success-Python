# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:47:14 2022

@author: Muriel
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Salam Alaikum Muriel !'

if __name__ == '__main__':
    app.run()
