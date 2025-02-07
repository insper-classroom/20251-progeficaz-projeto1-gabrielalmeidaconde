import json
from flask import abort

def load_data(nome):
    filepaths = f"static/data/{nome}"
    try:
        with open(filepaths, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        abort(404, description="Resource not found")

def load_template(nome):
    filepaths = f"static/templates/{nome}"
    try:
        with open(filepaths, 'r') as file:
            return file.read()
    except FileNotFoundError:
        abort(404, description="Resource not found")

def save_data(nome, data):
    filepaths = f"static/data/{nome}"
    try:
        with open(filepaths, 'w') as file:
            json.dump(data, file)
    except FileNotFoundError:
        abort(404, description="Resource not found")