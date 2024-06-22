import time
from UniqueIDGenerator import UniqueIDGenerator

def performance_test(generator, num_ids):
    start_time = time.time()
    for _ in range(num_ids):
        generator.generate_id()
    end_time = time.time()
    print(f"Generated {num_ids} IDs in {end_time - start_time} seconds")

generator = UniqueIDGenerator(node_id=1)
performance_test(generator, 10000000)
