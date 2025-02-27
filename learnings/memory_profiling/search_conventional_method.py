import json
from collections import deque
from memory_profiler import profile, memory_usage

# ==========================
# STEP 1: LOAD JSON FILE
# ==========================

@profile
def load_json(json_filename):
    """
    Loads the entire JSON file into memory.
    """
    with open(json_filename, "r") as file:
        return json.load(file)

# ==========================
# STEP 2: ITERATIVE SEARCH FUNCTION
# ==========================

@profile
def iterative_search(json_data, target_key):
    """
    Iteratively searches for a key at exactly 6 levels deep in a JSON structure.

    :param json_data: Loaded JSON data
    :param target_key: The key to search for
    :return: A list of found values
    """
    results = []  # Store found values
    queue = deque([(json_data, 0)])  # (current_dict, depth)

    while queue:
        current, depth = queue.popleft()

        if isinstance(current, dict):
            for key, value in current.items():
                if depth == 5 and key == target_key:  # 6th level (0-based index)
                    results.append(value)
                elif isinstance(value, (dict, list)):  # Traverse deeper
                    queue.append((value, depth + 1))

        elif isinstance(current, list):
            for item in current:
                if isinstance(item, (dict, list)):  # Traverse deeper
                    queue.append((item, depth))

    return results

# ==========================
# STEP 3: MEMORY PROFILING
# ==========================

def measure_memory_usage(func, *args):
    """
    Measures peak memory usage of a function.
    """
    mem_usage = memory_usage((func, args))
    print(f"Peak Memory Usage for {func.__name__}: {max(mem_usage):.2f} MB")

# ==========================
# STEP 4: RUN SCRIPT
# ==========================

if __name__ == "__main__":
    json_filename = "teams.json"
    search_key = "software_user_2"  # Example key to search

    # Load JSON into memory and measure memory usage
    teams_data = load_json(json_filename)

    # Perform iterative search and measure memory usage
    measure_memory_usage(iterative_search, teams_data, search_key)
