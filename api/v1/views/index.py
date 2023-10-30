#!/usr/bin/python3
""" 
This module defines routes for the index of the API.
The main route `/status` is used to check the status of the API.
"""

from models import storage
from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status", methods=["GET"], strict_slashes=False)
def get_api_status():
    """
    Retrieves the status of the API
    Returns: JSON response indicating the status of the API
    """
    return jsonify({"status": "OK"})

@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stat():
    """
    Retrieves the number of each objects by type
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
