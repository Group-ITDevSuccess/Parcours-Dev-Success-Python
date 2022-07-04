# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:55:25 2022

@author: Muriel
"""

from flask import Flask, request

app = Flask(import_name=__name__)

@app.route("/echo")
def echo():
    to_echo = request.args.get("echo","")
    response = "{}".format(to_echo)
    
    return response

if __name__ == "__main__":
    app.run()