from healthcheck import HealthCheck
import plotly_express as px
import plotly
import requests
from functools import wraps
from datetime import date, datetime, timedelta
import os
import base64
import logging
import json
import io
from flask import (Flask, flash, jsonify, make_response,
                   redirect, render_template, request, session, url_for)
print("flask imported.")

# Initialize Flask app
app = Flask(__name__)

# Initialize server connection health check
health = HealthCheck(app, "/hcheck")


def howami():
    return True, "Server connection OK, Thanks for checking :)"


health.add_check(howami)


@app.route("/")
def home():
    return "home page"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1",
            port=int(os.environ.get("PORT", 8080)))
