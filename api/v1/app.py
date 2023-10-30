#!/usr/bin/python3
"""
This module contains the principal application
"""

from flask import Flask

from models import storage
from api.v1.views import app_views

from os import getenv

""" Create a Flask instance"""
app = Flask(__name__)

"""" Register the app_views blueprint to the Flask instance """
app.register_blueprint(app_views)

""" Define a method to handle teardown_appcontext """
@app.teardown_appcontext
def close_storage(exception):
    """ Teardown method to close the storage """
    # print(exception)
    storage.close()

if __name__ == "__main__":
    """Get the host and port from environment variables or use defaults. """
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    """ Run the Flask server with the specified host and port. """
    app.run(host=host, port=port, threaded=True)
