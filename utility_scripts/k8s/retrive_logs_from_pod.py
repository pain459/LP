from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

# Replace with your pod name and namespace
pod_name = 'your-pod-name'
namespace = 'default'

logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)

print(f"Logs for {pod_name}:\n{logs}")
