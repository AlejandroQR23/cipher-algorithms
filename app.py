from flask import Flask, make_response, request

from data import algorithms, testing_vectors

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/algorithms')
def get_algorithms():
    cipher_algorithms = [
        {
            'name': algorithm['name'],
            'key_size': algorithm['key_size'],
            'description': algorithm['description']
        }
        for algorithm in algorithms.algorithms
    ]
    return make_response(cipher_algorithms, 200)


@app.route('/algorithms/average/<string:algorithm>')
def get_average_time(algorithm):
    iterations = int(request.args.get('iterations', 150))
    data = request.args.get('data', 'secret')

    for current_algorithm in algorithms.algorithms:
        if current_algorithm['name'] == algorithm:
            average_encrypt, average_decrypt = current_algorithm['get_avg'](
                iterations, data)
            return make_response({
                'avg_encrypt': average_encrypt,
                'avg_decrypt': average_decrypt
            }, 200)
    return make_response('Invalid algorithm', 400)


@app.route('/testing_vectors/<string:type>')
def get_testing_vectors(type):
    try:
        return make_response(testing_vectors.TESTING_VECTORS[type], 200)
    except KeyError:
        return make_response('Invalid type', 400)


if __name__ == '__main__':
    app.run(debug=True)
