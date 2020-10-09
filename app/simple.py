from random import randint
from secrets import choice
from string import ascii_letters
from flask import Flask, json, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/version")
def hello():
    return json_response(
        {
            "application": "Simple Api",
            "version": 0.1
         }
    )


@app.route("/randoms")
def randoms():
    return json_response(rnd())


@app.route("/hashname", methods=['POST'])
def hashname():
    content = request.json
    name = content['name']
    return json_response(hashit(name))


def json_response(data):
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


def rnd():
    rnum = randint(1, 80)
    rstr = ''.join(choice(ascii_letters) for _ in range(rnum))
    jsrnum = {
        "number": rnum,
        "string": rstr
    }
    return jsrnum


def hashit(name):
    jshash = {
        "name": name,
        "hash": hash(name.encode('utf-8'))
    }
    return jshash


if __name__ == "__main__":
    # threading.Thread(target=app.run).start()
    app.run(host="127.0.0.1", port=5000)
