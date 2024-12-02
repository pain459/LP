import requests
from flask import Flask, jsonify
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = Flask(__name__)

# OpenTelemetry setup
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
tracer_provider = TracerProvider()
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)
tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

@app.route("/", methods=["GET"])
def index():
    data = {"data": "test_string"}
    response = requests.post("http://service_b:5001/process", json=data)

    if response.status_code != 200:
        return jsonify({"error": "Service B failed", "details": response.json()}), response.status_code

    return jsonify({"message": "Request completed", "service_b_response": response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
