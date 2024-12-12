import os
import json
from collections import Counter
import time

DATALAKE_DIR = 'datalake'

def consolidate_metrics():
    # Read all metric files from the datalake directory
    metrics = []
    for filename in os.listdir(DATALAKE_DIR):
        if filename.endswith('.json'):
            file_path = os.path.join(DATALAKE_DIR, filename)
            with open(file_path, 'r') as f:
                metric = json.load(f)
                metrics.append(metric)

    # Aggregate counts of "up" and "down"
    statuses = [m['status'] for m in metrics]
    counter = Counter(statuses)

    # Example summary
    summary = {
        "total_metrics": len(metrics),
        "up_count": counter.get('up', 0),
        "down_count": counter.get('down', 0),
        "last_updated": int(time.time())
    }

    return summary

if __name__ == '__main__':
    summary = consolidate_metrics()
    print("Metrics Summary:")
    print(json.dumps(summary, indent=2))
