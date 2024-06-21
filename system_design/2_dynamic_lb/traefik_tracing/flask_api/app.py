from flask import Flask, jsonify, request
import time
import socket
from jaeger_client import Config
from flask_opentracing import FlaskTracing

app = Flask(__name__)

# Initialize Jaeger tracer
def init_tracer(service_name='flask-app'):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
        },
        service_name=service_name,
        validate=True,
    )
    return config.initialize_tracer()

# Initialize tracer
tracer = init_tracer()
# Initialize Flask tracing
flask_tracing = FlaskTracing(tracer, True, app)

@app.route('/api', methods=['GET'])
def api():
    with tracer.start_span('api') as span:
        span.set_tag('http.method', request.method)
        span.set_tag('http.url', request.url)
        span.set_tag('http.client_ip', request.remote_addr)
        
        response = {
            "time": int(time.time()),  # Current time in epoch UTC format
            "server": socket.gethostname()  # Server name
        }
        
        span.log_kv({'event': 'response', 'value': response})
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
