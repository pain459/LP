import json
from collections import deque
from memory_profiler import profile, memory_usage

# Load JSON conventionally
@profile
def load_json(json_filename):
    with open(json_filename, "r") as file:
        return json.load(file)

# Iterative search function
@profile
def iterative_search(json_data, target_key):
    results = []
    queue = deque([(json_data, 0)])  # (current_dict, depth)

    while queue:
        current, depth = queue.popleft()

        if isinstance(current, dict):
            for key, value in current.items():
                if depth >= 7 and key == target_key:  # 8th level (0-based index)
                    results.append(value)
                elif isinstance(value, (dict, list)):
                    queue.append((value, depth + 1))

        elif isinstance(current, list):
            for item in current:
                if isinstance(item, (dict, list)):
                    queue.append((item, depth))

    return results

# Measure memory usage
def measure_memory_usage(func, *args):
    mem_usage = memory_usage((func, args))
    print(f"Peak Memory Usage for {func.__name__}: {max(mem_usage):.2f} MB")

# Run search on generated JSON
if __name__ == "__main__":
    json_filename = "company_data.json"
    search_key = "unique_search_key"

    # Load JSON and measure memory
    company_data = load_json(json_filename)

    # Search for deeply nested key
    measure_memory_usage(iterative_search, company_data, search_key)
