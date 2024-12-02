from flask import Flask, jsonify
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

app = Flask(__name__)

# OpenTelemetry setup
FlaskInstrumentor().instrument_app(app)
tracer_provider = TracerProvider()
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)
tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

@app.route("/process")
def process():
    return jsonify({"message": "Processed successfully by Service B"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
