import time
import threading
import sys

class SnowflakeIDGenerator:
    def __init__(self, node_id):
        self.node_id = node_id
        self.node_id_bits = 10
        self.sequence_bits = 12
        self.max_node_id = (1 << self.node_id_bits) - 1
        self.max_sequence = (1 << self.sequence_bits) - 1

        if node_id > self.max_node_id:
            raise ValueError(f"Node ID {node_id} exceeds max node ID {self.max_node_id}")

        self.epoch = 1640995200000  # Custom epoch (e.g., Jan 1, 2022)
        self.last_timestamp = -1
        self.sequence = 0
        self.lock = threading.Lock()

    def _current_millis(self):
        return int(time.time() * 1000)

    def _wait_next_millis(self, last_timestamp):
        timestamp = self._current_millis()
        while timestamp <= last_timestamp:
            timestamp = self._current_millis()
        return timestamp

    def generate_id(self):
        with self.lock:
            timestamp = self._current_millis()

            if timestamp < self.last_timestamp:
                raise Exception("Clock moved backwards. Refusing to generate id")

            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & self.max_sequence
                if self.sequence == 0:
                    timestamp = self._wait_next_millis(self.last_timestamp)
            else:
                self.sequence = 0

            self.last_timestamp = timestamp

            id = ((timestamp - self.epoch) << (self.node_id_bits + self.sequence_bits)) | (self.node_id << self.sequence_bits) | self.sequence
            return id

def main(node_id):
    generator = SnowflakeIDGenerator(node_id)
    ids = set()

    num_ids_to_generate = 100000  # Generate 100,000 IDs per node

    for _ in range(num_ids_to_generate):
        ids.add(generator.generate_id())

    print(f"Node {node_id} generated {len(ids)} unique IDs.")

if __name__ == "__main__":
    node_id = int(sys.argv[1])
    main(node_id)
