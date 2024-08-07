# Hystrix Demo with Python Circuit Breaker

This is a simple demonstration of the circuit breaker pattern using Python and the `pybreaker` library.

## Running the Project

To run the project, simply execute:

```sh
python main.py


### 2. Binder Configuration Files

#### File: binder/postBuild
This script runs after the environment is built and can be used to perform additional setup.
```sh
#!/bin/bash
pip install -r requirements.txt
