import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Read the 'NAME' environment variable
    name = os.environ.get('NAME', 'World')

    # Output a personalized greeting
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

