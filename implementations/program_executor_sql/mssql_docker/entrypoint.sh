#!/bin/bash

# Delay for 30 seconds to allow MSSQL Server to boot up
echo "Waiting for MSSQL Server to start..."
sleep 3000

# Execute the Python script
echo "Executing Python script"
python connect_to_sql.py
