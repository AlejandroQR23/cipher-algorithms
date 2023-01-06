# Cipher App

This is a simple API that compares the average time of encryption and decryption of a given text using different algorithms.

## Installation

To run this app you need to create a python virtual environment and install the requirements.txt file.

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

After installing the requirements, you can run the app with the following command:

```bash
python app.py
```

This will run the app on debug mode. Also you can run it withou debug mode with the following command:

```bash
flask run
```

## Endpoints

#### GET /algorithms/

This endpoint returns a list of the available algorithms.

### GET /algorithms?type={type}

This endpoint returns a list of the available algorithms of the given type.

### GET /algorithms/average/{algorithm}?data={data}&iterations={iterations}

This endpoint returns the average time of encryption and decryption of the given data using the given algorithm and the given number of iterations.

### GET /algorithms/compare?algo1={algo1}&algo2={algo2}&data={data}&iterations={iterations}

This endpoint returns best algorithm time of encryption and decryption between the given algorithms using the given data and the given number of iterations.
