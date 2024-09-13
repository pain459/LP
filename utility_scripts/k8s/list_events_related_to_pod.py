from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

# Replace 'default' with your namespace
namespace = 'default'
events = v1.list_namespaced_event(namespace)

for event in events.items:
    if event.involved_object.kind == "Pod":
        print(f"Event Type: {event.type}")
        print(f"Reason: {event.reason}")
        print(f"Message: {event.message}")
        print(f"Pod: {event.involved_object.name}")
        print("-" * 40)
