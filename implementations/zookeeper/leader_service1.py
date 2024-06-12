from kazoo.client import KazooClient
import time

def leader_election():
    zk = KazooClient(hosts='127.0.0.1:2181,127.0.0.1:2182,127.0.0.1:2183')
    zk.start()

    @zk.DataWatch("/leader")
    def watch_node(data, stat, event):
        if event and event.type == "DELETED":
            print("Leader node deleted, starting leader election")
            become_leader()

    def become_leader():
        try:
            zk.create("/leader", b"Service 1", ephemeral=True)
            print("Service 1 is now the leader")
        except:
            print("Service 1 failed to become the leader")

    become_leader()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    leader_election()
