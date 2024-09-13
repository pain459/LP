from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

# Replace 'default' with your namespace
namespace = 'default'
pods = v1.list_namespaced_pod(namespace)

for pod in pods.items:
    if pod.status.phase == 'Pending':
        print(f"Pending Pod: {pod.metadata.name}")
        conditions = pod.status.conditions or []
        for condition in conditions:
            if condition.type == 'PodScheduled' and condition.status == 'False':
                print(f"Reason: {condition.reason}")
                print(f"Message: {condition.message}")
                print("-" * 40)
