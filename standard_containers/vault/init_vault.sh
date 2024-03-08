#!/bin/bash

# Initialize Vault
vault operator init > /tmp/init_output

# Unseal Vault
while [ $(grep "Unseal Key" /tmp/init_output | wc -l) -lt 3 ]; do
    echo "Waiting for initialization to complete..."
    sleep 2
done

for i in $(seq 1 3); do
    vault operator unseal $(grep "Unseal Key $i" /tmp/init_output | awk '{print $NF}')
done

# Enable Key/Value secrets engine
vault secrets enable -path=secrets kv
