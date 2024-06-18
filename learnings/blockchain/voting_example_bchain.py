import hashlib
import time

# Block class to represent each vote as a block in the blockchain
class Block:
    def __init__(self, index, previous_hash, timestamp, voter_id, candidate, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.voter_id = voter_id
        self.candidate = candidate
        self.hash = hash

# Function to calculate the hash of a block
def calculate_hash(index, previous_hash, timestamp, voter_id, candidate):
    value = str(index) + str(previous_hash) + str(timestamp) + str(voter_id) + str(candidate)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Function to create the genesis block (first block in the blockchain)
def create_genesis_block():
    return Block(0, "0", int(time.time()), "0", "Genesis", calculate_hash(0, "0", int(time.time()), "0", "Genesis"))

# Function to create a new block (vote) and link it to the previous block
def create_new_block(previous_block, voter_id, candidate):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, voter_id, candidate)
    return Block(index, previous_block.hash, timestamp, voter_id, candidate, hash)

# Function to validate the integrity of the blockchain
def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        
        # Check if the hash of the block is correct
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.voter_id, current_block.candidate):
            return False
        
        # Check if the block is properly linked to the previous block
        if current_block.previous_hash != previous_block.hash:
            return False
        
    return True

# Function to tally votes for each candidate
def tally_votes(blockchain):
    votes = {}
    for block in blockchain[1:]:  # Skip the genesis block
        if block.candidate in votes:
            votes[block.candidate] += 1
        else:
            votes[block.candidate] = 1
    return votes

# Initialize blockchain with the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Function to cast a vote and add it to the blockchain
def cast_vote(voter_id, candidate):
    global previous_block
    new_block = create_new_block(previous_block, voter_id, candidate)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Voter {voter_id} has voted for {candidate}. Block #{new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}\n")

# Example of casting votes
cast_vote("Voter1", "CandidateA")
cast_vote("Voter2", "CandidateB")
cast_vote("Voter3", "CandidateA")

# Verify blockchain integrity
print("Blockchain valid:", is_chain_valid(blockchain))

# Tally votes and display the results
votes = tally_votes(blockchain)
print("Vote tally:", votes)
