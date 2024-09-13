from kubernetes import client, config, stream

config.load_kube_config()

v1 = client.CoreV1Api()

# Replace with your pod name, namespace, and command
pod_name = 'your-pod-name'
namespace = 'default'
exec_command = ['/bin/sh', '-c', 'echo Hello from within the pod']

resp = stream.stream(v1.connect_get_namespaced_pod_exec,
                     pod_name,
                     namespace,
                     command=exec_command,
                     stderr=True, stdin=False,
                     stdout=True, tty=False)

print(resp)
