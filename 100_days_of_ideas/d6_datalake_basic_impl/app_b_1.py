import os
import json
from collections import Counter
from datetime import datetime

DATALAKE_DIR = 'datalake'

def consolidate_metrics_for_date(year, month, day):
    # Construct the partition path
    partition_path = os.path.join(DATALAKE_DIR, f"{year:04d}", f"{month:02d}", f"{day:02d}")
    if not os.path.exists(partition_path):
        return None

    metrics = []
    # Find all jsonl files in the directory
    for filename in os.listdir(partition_path):
        if filename.endswith('.jsonl'):
            filepath = os.path.join(partition_path, filename)
            with open(filepath, 'r') as f:
                for line in f:
                    if line.strip():
                        metric = json.loads(line.strip())
                        metrics.append(metric)

    # Aggregate counts
    statuses = [m['status'] for m in metrics]
    counter = Counter(statuses)
    summary = {
        "total_metrics": len(metrics),
        "up_count": counter.get('up', 0),
        "down_count": counter.get('down', 0),
        "date": f"{year:04d}-{month:02d}-{day:02d}"
    }
    return summary

if __name__ == '__main__':
    # Example: Consolidate metrics for today's date
    now = datetime.utcnow()
    summary = consolidate_metrics_for_date(now.year, now.month, now.day)
    if summary:
        print("Metrics Summary for today:")
        print(json.dumps(summary, indent=2))
    else:
        print("No metrics found for today.")
