import ijson
from memory_profiler import profile, memory_usage

# ==========================
# STEP 1: STREAMING SEARCH FUNCTION
# ==========================

@profile
def search_deep_key_ijson(json_file, target_key):
    """
    Uses ijson to efficiently search for a deeply nested key in a large JSON file.
    
    :param json_file: Path to the JSON file
    :param target_key: The key to search for
    :return: A generator yielding found values
    """
    with open(json_file, 'rb') as f:
        parser = ijson.parse(f)
        key_stack = []
        value_found = False

        for prefix, event, value in parser:
            if event == 'map_key':
                key_stack.append(value)

                # If we reach 8 levels deep and the key matches
                if len(key_stack) >= 8 and key_stack[-1] == target_key:
                    value_found = True  # Mark flag to capture the value

            elif value_found and event in ('string', 'number', 'boolean', 'null'):
                print(f"Found {target_key}: {value}")  # Print the found value
                value_found = False  # Reset flag

            elif event in ('end_map', 'end_array'):  # Backtracking when structure ends
                if key_stack:
                    key_stack.pop()

# ==========================
# STEP 2: MEMORY PROFILING
# ==========================

def measure_memory_usage(func, *args):
    """
    Measures peak memory usage of a function.
    """
    mem_usage = memory_usage((func, args))
    print(f"Peak Memory Usage for {func.__name__}: {max(mem_usage):.2f} MB")

# ==========================
# STEP 3: RUN SCRIPT
# ==========================

if __name__ == "__main__":
    json_filename = "company_data.json"
    search_key = "unique_search_key"  # Example key to search

    # Perform streaming search and measure memory usage
    measure_memory_usage(search_deep_key_ijson, json_filename, search_key)
