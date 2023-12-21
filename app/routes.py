#!/usr/bin/env python3
"""
this is the route file which contain the URL
"""

from app import app


@app.route("/")
@app.route("/index")
def index():
    return "hello world"