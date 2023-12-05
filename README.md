# Blockchain Implementation with Flask

This project implements a simple blockchain using Python and Flask. The blockchain consists of a series of blocks containing proof-of-work and is accessible through a Flask-based web application.

## Installation

Ensure you have the required dependencies installed:

- Flask==0.12.2: `pip install Flask==0.12.2`
- Postman HTTP Client: [Postman Download](https://www.getpostman.com/)

## Usage

1. Run the Python script to start the Flask web application.
    ```bash
    python blockchain.py
    ```

2. Use Postman or any other HTTP client to interact with the blockchain API.

## Testing the Smart Contract

### Using Remix

[Remix](https://remix.ethereum.org/) is an online Solidity IDE that allows you to compile, deploy, and test your smart contracts. Follow these steps to test the smart contract using Remix:

1. Open Remix in your web browser.

2. Copy and paste the smart contract code into the Remix editor.

3. Compile the smart contract by clicking on the "Solidity Compiler" tab and then clicking the "Compile" button.

4. Switch to the "Deploy & Run Transactions" tab.

5. Under the "Deploy" section, select the appropriate environment (JavaScript VM for an in-memory blockchain or Injected Web3 for interacting with an external Ethereum node).

6. Click the "Deploy" button to deploy your smart contract.

7. Interact with your smart contract using the Remix interface to test its functionality.

### Using Ganache

[Ganache](https://www.trufflesuite.com/ganache) is a personal blockchain for Ethereum development that you can use to deploy and test smart contracts. Follow these steps to test the smart contract using Ganache:

1. Download and install Ganache from the official website.

2. Open Ganache and start a new workspace, configuring the desired settings such as the number of accounts, gas limit, and network.

3. Once Ganache is running, deploy your smart contract to the Ganache blockchain using a development environment like Truffle or Remix.

4. Interact with your deployed smart contract using tools like Remix, MyEtherWallet, or custom scripts.

5. Use Ganache's user interface to inspect transactions, events, and account balances for testing purposes.

Remember to update any relevant configuration settings in your smart contract (e.g., contract addresses, endpoints) to match the environment you are deploying to (Remix or Ganache).

## API Endpoints

### 1. Mine a New Block

#### Endpoint:

- `/mine_block` (GET)

#### Description:

Mines a new block and adds it to the blockchain.

#### Example:

- Request:
  ```bash
  GET http://localhost:5000/mine_block

### Notes
This is a simple demonstration of blockchain functionality and is not intended for production use.
Ensure Flask is running on host 0.0.0.0 and port 5000 to allow external access.
Use Postman or a similar tool to make HTTP requests to the provided endpoints.
Feel free to explore and modify the code to enhance or adapt it for your specific needs!
