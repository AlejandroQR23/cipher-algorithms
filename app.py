from flask import Flask, make_response, request

from data import algorithms, testing_vectors
from utils.helpers import get_algorithm, get_best_time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/algorithms')
def get_algorithms():
    type_filter = request.args.get('type', None)
    cipher_algorithms = [
        {
            'name': algorithm['name'],
            'key_size': algorithm['key_size'],
            'description': algorithm['description'],
            'type': algorithm['type']
        }
        for algorithm in algorithms.algorithms
    ]
    if type_filter:
        cipher_algorithms = [
            algorithm for algorithm in cipher_algorithms
            if algorithm['type'] == type_filter
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


@app.route('/algorithms/compare')
def compare_algorithms():
    iterations = int(request.args.get('iterations', 150))
    data = request.args.get('data', 'secret')
    algo1 = request.args.get('algo1', None)
    algo2 = request.args.get('algo2', None)

    if algo1 and algo2:
        selected_algorithm1 = get_algorithm(algo1)
        selected_algorithm2 = get_algorithm(algo2)
        if selected_algorithm1 and selected_algorithm2:
            if selected_algorithm1['type'] != selected_algorithm2['type']:
                return make_response('Algorithms must be of the same type', 400)
            try:
                best_encryption, best_decryption = get_best_time(
                    selected_algorithm1, selected_algorithm2, iterations, data)
                response = {
                    'best_encryption': best_encryption,
                }
                if best_decryption:
                    response['best_decryption'] = best_decryption
                return make_response(response, 200)
            except ValueError as e:
                return make_response(str(e), 400)
        return make_response('Invalid algorithm', 400)
    return make_response('Missing algorithm: You must provide two algorithms to compare', 400)


@app.route('/testing_vectors/<string:type>')
def get_testing_vectors(type):
    try:
        return make_response(testing_vectors.TESTING_VECTORS[type], 200)
    except KeyError:
        return make_response('Invalid type', 400)


if __name__ == '__main__':
    app.run(debug=True)
