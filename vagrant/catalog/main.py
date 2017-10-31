from flask import Flask, session, flash, redirect, render_template, request, url_for, make_response
import random
import string
import json
from oauth2client import client, crypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Initialize Flask-App
app = Flask(__name__)




# Run flask app
if __name__ == '__main__':
    # app.debug = True
    app.secret_key = "not_very_secretive"
    app.run(host='0.0.0.0', port=8080)