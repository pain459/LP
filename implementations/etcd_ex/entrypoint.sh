#!/bin/bash

if [ -f /backup/etcd-snapshot.db ]; then
    echo "Restoring etcd data from backup..."
    # Run etcdctl command to restore the backup
    etcdctl snapshot restore /backup/etcd-snapshot.db \
        --data-dir /etcd-data \
        --initial-cluster-token etcd-cluster-token \
        --initial-advertise-peer-urls http://etcd:2380 \
        --name etcd-node \
        --initial-cluster etcd-node=http://etcd:2380 \
        --initial-cluster-state new
fi

# Start the FastAPI server
uvicorn app:app --host 0.0.0.0 --port 5000
