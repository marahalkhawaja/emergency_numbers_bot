from flask import Flask, jsonify

from emergency_data import EMERGENCY_SERVICES

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Emergency Numbers API"})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/services")
def list_services():
    services = [
        {"id": service_id, **service}
        for service_id, service in EMERGENCY_SERVICES.items()
    ]
    return jsonify(services)


@app.get("/services/<service_id>")
def get_service(service_id):
    service = EMERGENCY_SERVICES.get(service_id)
    if service is None:
        return jsonify({"error": "Service not found"}), 404

    return jsonify({"id": service_id, **service})
