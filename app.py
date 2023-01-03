from flask import Flask, make_response, request

from data import algorithms, testing_vectors
from utils.helpers import get_algorithm

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

    selected_algorithm = get_algorithm(algorithm)
    if selected_algorithm:
        try:
            average_encrypt, average_decrypt = selected_algorithm['get_avg'](
                iterations, data)

            response = {
                'avg_encrypt_time': average_encrypt,
            }
            if average_decrypt:
                response['avg_decrypt_time'] = average_decrypt
            return make_response(response, 200)
        except KeyError:
            return make_response('Average not implemented yet', 400)
        except ValueError as e:
            return make_response(str(e), 400)
    return make_response('Invalid algorithm', 400)


@app.route('/testing_vectors/<string:type>')
def get_testing_vectors(type):
    try:
        return make_response(testing_vectors.TESTING_VECTORS[type], 200)
    except KeyError:
        return make_response('Invalid type', 400)


if __name__ == '__main__':
    app.run(debug=True)
