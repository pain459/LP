#!/bin/bash

# Set the master password and database name
MASTER_PASSWORD="supersecretpassword"

# Create the realm non-interactively
echo -e "$MASTER_PASSWORD\n$MASTER_PASSWORD" | krb5_newrealm

# Add admin principal
echo -e "admin\nadmin" | kadmin.local -q "addprinc -pw admin admin/admin"

# Add the principal to the keytab
kadmin.local -q "ktadd admin/admin"
