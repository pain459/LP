from kubernetes import client, config

config.load_kube_config()

custom_api = client.CustomObjectsApi()

# Fetch metrics for pods
metrics = custom_api.list_cluster_custom_object(group="metrics.k8s.io", version="v1beta1", plural="pods")

for item in metrics['items']:
    pod_name = item['metadata']['name']
    containers = item['containers']
    print(f"Pod: {pod_name}")
    for container in containers:
        name = container['name']
        cpu = container['usage']['cpu']
        memory = container['usage']['memory']
        print(f"  Container: {name}")
        print(f"    CPU Usage: {cpu}")
        print(f"    Memory Usage: {memory}")
    print("-" * 40)
