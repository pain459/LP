import time
import threading

class UniqueIDGenerator:
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

# Example usage
generator = UniqueIDGenerator(node_id=1)
for _ in range(10):
    print(generator.generate_id())
