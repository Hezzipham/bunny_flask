# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app import app, db

# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)