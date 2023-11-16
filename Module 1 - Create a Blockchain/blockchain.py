# Module 1 - Create a Blockchain

# To be installed: 
    #Flask==0.12.2: pip install Flask==0.12.2
    #Postman HTTP Client: https://www.getpostman.com/

# Import Libraries
    # datetime to timestamp each block
import datetime
    # hashlib library to hash the blocks
import hashlib
    # Need the json loiubrary for its dumps function to encode the blocks before we hash them
import json
    # From flask, we will need the Flask class to create an object of the flask class to make the web application 
    # jsonify is a function used to return the messages in postman when we interact with postman
from flask import Flask, jsonify