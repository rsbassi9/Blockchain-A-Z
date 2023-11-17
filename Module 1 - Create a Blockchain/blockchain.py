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

# Part 1 - Building a Blockchain
class Blockchain:
    
    def __init__(self):
        self.chain = []     # Variable for The chain containing the blocks initialized as a list
        self.create_block(proof = 1, previous_hash = '0')    # Variable for Genesis block, created using the create_block function. arguments: proof = arbitrary number, previous hash (arbitraty for genesis block)
        
   
    # Define a new create block function that will to be implemented right after mining a block
    # It will get the proof of work needed to be solved. once solved, a new block is created and 
    # will be added to the blockchain. The new block will contain the index, the timestamp, proof and previous hash
    def create_block(self, proof, previous_hash):
        
        # Variable block is a dictionary containing each block, with 4 essential keys: index of block, timestamp, proof of the block, previous hash. This can potentiall include transactions, cryptocurrency
        block = {'index' : len(self.chain) + 1,
                 'timestamp' : str(datetime.datetime.now()), #Make the datetime a string for json format
                 'proof' : proof,
                 'previous_hash' : previous_hash} 
        self.chain.append(block) # add the newly created block to the chain
        return block # return the block for display in postman
    
    # Define a function to get the last block of the current chain we are dealing with at any time
    def get_previous_block(self):
        return self.chain[-1]   # Get the last index of the chain
    
    # Define a proof of work - hard to solve, easy to verify
    # Previous prrof is an element of the problem that miners will need to coonsider to find the new proof
    def proof_of_work(self, previous_proof):
        new_proof = 1      # Problem is solved through trial and error, incrementing the proof each time, starting at 1
        check_proof = False     # Initialize to False. When we run the loop and the new proof is found, this turns to true
        while check_proof is False:      # Define the problem the miners need to solve for check_proof to be true: 4 leading zero problem using SHA256. (the more the leading zeros, the harder the problem is to solve)
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()    # The hash function needs to be non-symmetrical , ie the function read forward is not eaqual to the function read backwards. This can be made as challenging as you like.encode and hexdigest dunctions used to output the hash function in the correct format
            if hash_operation[:4] == '0000':        # If the hash output has 4 leading zeros, then check_proof is true, the block can be mined
                check_proof = True
            else:                                   # If false, we give the iteration another try adn increment new_proof by 1
                new_proof += 1
        
        
# Part 2 - Mining our Blockchain