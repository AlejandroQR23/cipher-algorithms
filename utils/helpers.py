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
