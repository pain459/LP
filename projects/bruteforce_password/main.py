import itertools
import hashlib
import multiprocessing
import time

def hash_password(password):
    """
    Hash the password using SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def map_function(character_set, length, prefix=""):
    """
    Generate all possible combinations of the given length using the character set.
    """
    if length == 0:
        yield prefix
    else:
        for char in character_set:
            yield from map_function(character_set, length - 1, prefix + char)

def reduce_function(args):
    """
    Check if the combination matches the hashed password.
    """
    combination, hashed_password = args
    if hash_password(combination) == hashed_password:
        return combination
    return None

def chunked_combinations(character_set, length, chunk_size):
    """
    Generate all possible combinations of the given length and chunk them.
    """
    combinations = map_function(character_set, length)
    chunk = []
    for combination in combinations:
        chunk.append(combination)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def parallel_map_reduce(character_set, hashed_password, max_length, chunk_size, num_workers=None):
    """
    Parallel MapReduce implementation for brute-forcing a password.
    """
    if num_workers is None:
        num_workers = multiprocessing.cpu_count()
    
    start_time = time.time()

    with multiprocessing.Pool(num_workers) as pool:
        for length in range(1, max_length + 1):
            for chunk in chunked_combinations(character_set, length, chunk_size):
                args = [(combo, hashed_password) for combo in chunk]
                results = pool.map(reduce_function, args)
                for result in results:
                    if result:
                        pool.terminate()  # Stop all workers as soon as the password is found
                        end_time = time.time()
                        return {
                            "found_password": result,
                            "time_taken": end_time - start_time
                        }

    end_time = time.time()
    return {
        "found_password": None,
        "time_taken": end_time - start_time
    }

# Example usage
if __name__ == "__main__":
    character_set = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = "abc123"
    hashed_password = hash_password(password)  # Using the hash_password function to generate the hashed password
    
    print(f"Hashed Password: {hashed_password}")
    
    # Perform MapReduce brute force
    result = parallel_map_reduce(character_set, hashed_password, max_length=6, chunk_size=1000)
    
    if result["found_password"]:
        print(f"Password found: {result['found_password']}")
    else:
        print("Password not found.")
    
    print(f"Time taken: {result['time_taken']} seconds")
