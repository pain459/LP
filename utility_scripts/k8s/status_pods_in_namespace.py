from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

v1 = client.CoreV1Api()

# Replace 'default' with your namespace
namespace = 'default'
pods = v1.list_namespaced_pod(namespace)

for pod in pods.items:
    print(f"Pod Name: {pod.metadata.name}")
    print(f"Status: {pod.status.phase}")
    print(f"Node Name: {pod.spec.node_name}")
    print("-" * 40)
