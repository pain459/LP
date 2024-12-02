import time
from flask import Flask, jsonify, request
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = Flask(__name__)

# OpenTelemetry setup
FlaskInstrumentor().instrument_app(app)
tracer_provider = TracerProvider()
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)
tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

@app.route("/transform", methods=["POST"])
def transform():
    request_data = request.json
    if not request_data or "data" not in request_data:
        return jsonify({"error": "Invalid request, 'data' key missing"}), 400

    original_data = request_data["data"]
    if not isinstance(original_data, str):
        return jsonify({"error": "'data' value must be a string"}), 400

    # Simulate processing delay
    time.sleep(2)

    transformed_data = {"original": original_data, "transformed": original_data.upper()}
    return jsonify(transformed_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
