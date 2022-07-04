# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:08:46 2022

@author: Muriel
"""

from flask import Flask, request

app = Flask(import_name=__name__)

@app.route("/echo", methods=["POST"])

def echo():
    name = request.values.get("name","")
    to_echo = request.values.get("echo","")
    
    response = "Salam Alaikum {} ! Tu as dis {}".format(name, to_echo)
    
    return response

app.run()