from kubernetes import client, config
from pprint import pprint

config.load_kube_config()

v1 = client.CoreV1Api()

# Replace with your pod name and namespace
pod_name = 'your-pod-name'
namespace = 'default'

pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)

pprint(pod)
