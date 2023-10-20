from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

phrases = [
    "Get ready to be inspired…", 
    "See rejection as redirection.",
    "There is beauty in simplicity.",
    "You can’t be late until you show up.",
    "Maybe life is testing you. Don’t give up.",
    "Impossible is just an opinion.",
    "Alone or not you gonna walk forward.",
]

# Original route
# @app.route('/')
# def get_random_quote():
#     return jsonify(random.choice(phrases))

@app.route('/')
def get_random_quote():
    return jsonify(random.choice(phrases))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

