from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

namespace = 'default'
pods = v1.list_namespaced_pod(namespace)

for pod in pods.items:
    if pod.status.phase == 'Pending':
        for condition in pod.status.conditions or []:
            if condition.reason == 'ErrImagePull' or condition.reason == 'ImagePullBackOff':
                print(f"Pod: {pod.metadata.name}")
                print(f"Reason: {condition.reason}")
                print(f"Message: {condition.message}")
                print("-" * 40)
