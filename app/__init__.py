"""DevOpsFlow Flask application factory."""

from flask import Flask, jsonify


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(JSON_SORT_KEYS=False)
    if test_config:
        app.config.update(test_config)

    @app.get("/")
    def index():
        return jsonify(
            name="DevOpsFlow",
            description="A containerized service delivered through an automated CI/CD pipeline.",
            version=app.config.get("APP_VERSION", "1.0.0"),
            endpoints=["/", "/health", "/ready"],
        )

    @app.get("/health")
    def health():
        return jsonify(status="healthy"), 200

    @app.get("/ready")
    def ready():
        return jsonify(status="ready"), 200

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify(error="Not found"), 404

    return app
