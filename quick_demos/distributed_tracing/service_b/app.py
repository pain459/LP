import requests
from flask import Flask, jsonify, request
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

@app.route("/process", methods=["POST"])
def process():
    request_data = request.json
    if not request_data or "data" not in request_data:
        return jsonify({"error": "Invalid request, 'data' key missing"}), 400

    response = requests.post("http://service_c:5002/transform", json={"data": request_data["data"]})

    if response.status_code != 200:
        return jsonify({"error": "Service C failed", "details": response.json()}), response.status_code

    return jsonify({"processed": response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
