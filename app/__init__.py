#!/usr/bin/env python3
"""
this will initialize the flask
"""

from flask import Flask

app = Flask(__name__)

from app import routes