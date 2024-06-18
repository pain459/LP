import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

def calculate_hash(index, previous_hash, timestamp, data, nonce):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(nonce)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block", 0), 0)

def mine_block(index, previous_hash, timestamp, data, difficulty):
    nonce = 0
    while True:
        hash = calculate_hash(index, previous_hash, timestamp, data, nonce)
        if hash.startswith('0' * difficulty):
            return Block(index, previous_hash, timestamp, data, hash, nonce)
        nonce += 1

def is_chain_valid(blockchain, difficulty):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data, current_block.nonce):
            return False
        
        if current_block.previous_hash != previous_block.hash:
            return False
        
        if not current_block.hash.startswith('0' * difficulty):
            return False
        
    return True

# Initialize blockchain
difficulty = 4
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the blockchain
num_of_blocks_to_add = 10

for i in range(num_of_blocks_to_add):
    new_block_data = f"Block #{i + 1} data"
    block_to_add = mine_block(previous_block.index + 1, previous_block.hash, int(time.time()), new_block_data, difficulty)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print(f"Block #{block_to_add.index} has been added to the blockchain!")
    print(f"Hash: {block_to_add.hash}")
    print(f"Nonce: {block_to_add.nonce}\n")

# Verify blockchain integrity
print("Blockchain valid:", is_chain_valid(blockchain, difficulty))
