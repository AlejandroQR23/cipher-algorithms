from flask import Flask, make_response

from data import algorithms, testing_vectors

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/algorithms')
def get_algorithms():
    return make_response(algorithms.algorithms)


@app.route('/testing_vectors/<string:type>')
def get_testing_vectors(type):
    try:
        return make_response(testing_vectors.TESTING_VECTORS[type], 200)
    except KeyError:
        return make_response('Invalid type', 400)


if __name__ == '__main__':
    app.run(debug=True)
