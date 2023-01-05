from data import algorithms


def get_algorithm(name):
    """
    Gets an algorithm from the algorithms list
    :param name: The name of the algorithm
    """
    for algorithm in algorithms.algorithms:
        if algorithm['name'] == name:
            return algorithm
    return None


def get_best_time(algo1, algo2, iterations, data):
    """
    Gets the best time between two algorithms
    """
    encryption_time, decryption_time = algo1['get_avg'](iterations, data)
    encryption_time2, decryption_time2 = algo2['get_avg'](iterations, data)

    print(f'Encryption time: {encryption_time} vs {encryption_time2}')
    print(f'Decryption time: {decryption_time} vs {decryption_time2}')

    if encryption_time < encryption_time2:
        best_encryption = {
            'time': encryption_time,
            'name': algo1['name'],
            'difference': encryption_time2 - encryption_time
        }
    else:
        best_encryption = {
            'time': encryption_time2,
            'name': algo2['name'],
            'difference': encryption_time - encryption_time2
        }

    best_decryption = None
    if decryption_time != None and decryption_time2 != None:
        if decryption_time < decryption_time2:
            best_decryption = {
                'time': decryption_time,
                'name': algo1['name'],
                'difference': decryption_time2 - decryption_time
            }
        else:
            best_decryption = {
                'time': decryption_time2,
                'name': algo2['name'],
                'difference': decryption_time - decryption_time2
            }

    return best_encryption, best_decryption
