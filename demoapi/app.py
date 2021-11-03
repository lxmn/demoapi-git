import sys
import os

from flask import Flask
from flask_restful import Resource, Api

from resources.hello_world import HelloWorld


app = Flask(__name__)
api = Api(app)
port = 5000


# Add all resources here
api.add_resource(HelloWorld, '/') # resource_class_kwargs={ 'port': port })


if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=port, debug=True)
    app.run(port=port, debug=True)