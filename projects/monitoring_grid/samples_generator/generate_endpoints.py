import yaml
import random

services = []
num_genesis = 25
num_dependents = 50
num_potentials = 25

all_services = [f'service{i}' for i in range(1, 101)]

for i in range(1, num_genesis + 1):
    genesis_service = {
        'name': f'service{i}',
        'genesis': {'host': f'service{i}', 'port': 80},
        'dependents': [],
        'potentials': []
    }
    dependents = random.sample(all_services, random.randint(1, 5))
    potentials = random.sample(all_services, random.randint(1, 5))

    for dependent in dependents:
        if dependent != f'service{i}':
            genesis_service['dependents'].append({'host': dependent, 'port': 80})

    for potential in potentials:
        if potential != f'service{i}':
            genesis_service['potentials'].append({'host': potential, 'port': 80})

    services.append(genesis_service)

endpoints = {'apis': services}

with open('endpoints.yaml', 'w') as file:
    yaml.dump(endpoints, file)
