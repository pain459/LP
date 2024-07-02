services = []
for i in range(1, 101):
    services.append(f'''
  service{i}:
    image: python:3.9-slim
    container_name: service{i}
    command: ["python", "-m", "http.server", "80"]
    deploy:
      resources:
        limits:
          memory: 50M
    networks:
      - monitor_net
''')

docker_compose = f'''version: '3.7'

services:
{''.join(services)}
  monitor:
    build: .
    container_name: monitor
    volumes:
      - .:/app
    command: ["python", "/app/monitor.py"]
    depends_on:
{''.join([f"      - service{i}\n" for i in range(1, 101)])}
    networks:
      - monitor_net

networks:
  monitor_net:
    driver: bridge
'''

with open('docker-compose.yml', 'w') as file:
    file.write(docker_compose)
