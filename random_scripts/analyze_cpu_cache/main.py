import psutil
import cpuinfo
import os

def get_cpu_cache_info():
    info = cpuinfo.get_cpu_info()

    print("=== CPU Cache Metrics ===")
    print(f"Brand: {info['brand_raw']}")
    print(f"Architecture: {info['arch']}")
    print(f"Cores (Physical): {psutil.cpu_count(logical=False)}")
    print(f"Cores (Logical): {psutil.cpu_count(logical=True)}")
    
    # Extract cache sizes (if available)
    if "l1_data_cache_size" in info:
        print(f"L1 Cache (Data): {info['l1_data_cache_size']}")
    if "l1_instruction_cache_size" in info:
        print(f"L1 Cache (Instruction): {info['l1_instruction_cache_size']}")
    if "l2_cache_size" in info:
        print(f"L2 Cache: {info['l2_cache_size']}")
    if "l3_cache_size" in info:
        print(f"L3 Cache: {info['l3_cache_size']}")

    # Additional cache info (if available)
    if "cache_line_size" in info:
        print(f"Cache Line Size: {info['cache_line_size']} bytes")
    if "cache_associativity" in info:
        print(f"Cache Associativity: {info['cache_associativity']}")

    print("="*30)

def get_cache_performance():
    """
    This function uses OS-specific commands to retrieve CPU cache performance stats.
    """
    print("\n=== Cache Performance Stats ===")
    
    if os.name == 'nt':  # Windows
        os.system("wmic cpu get L2CacheSize, L3CacheSize")
    elif os.path.exists("/proc/cpuinfo"):  # Linux
        os.system("lscpu | grep 'cache'")
    elif os.path.exists("/sys/devices/system/cpu/cpu0/cache"):
        os.system("find /sys/devices/system/cpu/cpu*/cache/index*/size -exec cat {} +")
    else:
        print("Cache performance stats are not available for this OS.")
    
    print("="*30)

if __name__ == "__main__":
    get_cpu_cache_info()
    get_cache_performance()
