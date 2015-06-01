#!/usr/bin/python2
# -*- coding: utf-8 -*-

from flask import *
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

with open('countries.json', 'ro') as f:
    data = {c['cca2']: c for c in json.load(f)}


@app.route('/countries/<code>')
def find_country(code):
    if code in data:
        return jsonify(data[code])
    else:
        return jsonify({}), 404


if __name__ == "__main__":
    app.run(use_debugger=False, debug=True, use_reloader=True, host='0.0.0.0')
