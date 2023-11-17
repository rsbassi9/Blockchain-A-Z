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
        return new_proof
    
    # Implement a function to check if the previous block hash matches, and if the proof of work has been solved (with 4 leading 0's)
    # It will return the cyptographic hash of our block
    def hash(self, block):
       encoded_block = json.dumps(block, sort_keys = True).encode()                        # Encode our block so it can be accepted by the SHA256 function. dumps function used to make the block dictionary a string. encode into the ocrrect format
       return hashlib.sha256(encoded_block).hexdigest()
   
    # Make the final function to return true if everything is right in the blockchain (if each block has a valid POW and the previous hash of a block is equal to the hash of the previous block)
    # Chain is an argument, since we will need to perform this check on each block in the chain - loop through each blocks index for this
    def is_chain_valid(self, chain):
        previous_block = chain[0]  # Initial parameters of the blockchain, starting at block 1
        block_index = 1
        while block_index < len(chain):   # Loop until we reach the final index of the chain
            # perform the 2 checks
            # Check 1:
            block = chain[block_index]      # The current block
            if block['previous_hash'] != self.hash(previous_block):   # If the 'previous_hash' of the current block is different from the hash of the previous_block, the chain is not valid - return false
                return False 
            # Check 2: check if the hash operation starts with 4 0's
            previous_proof = previous_block['proof']  # Get the proof key of the previous block
            proof = block['']    # Get the proof of the current block
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block     # Update our loop variable block index and our previous block variable. In the next iteration, the previous block becomes the current block
            block_index += 1
        return True
    
        
# Part 2 - Mining our Blockchain

# Creating a Web App using Flask
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()  # Get the previous block of the chain so we can check its proof
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)  # Proof of the future new block that will be added to the blockchain
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)  # returns the block and appends it to the blockchain
    # To be displayed in Postman:
    response = {'message' : 'Congratulations, you just mined a block!',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash']} 
    return jsonify(response), 200   # 200 = HTTP status code indication everything is OK with the request:  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes          

# Getting the full Blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain' : blockchain.chain,
                'length' : len(blockchain.chain)}   # We will also retreive the length of the blockchain so that we can keep track of it as it grows
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message' : 'All good. The block chain is valid.'}
    else:
        response = {'message' : 'Houston, we have a problem. The Blockchain is not valid' }
    return jsonify(response), 200
    
# Running the app
app.run(host = '0.0.0.0', port = 5000)

