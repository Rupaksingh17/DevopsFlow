from app import create_app


def test_home_returns_project_metadata():
    client = create_app({"TESTING": True, "APP_VERSION": "test"}).test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["name"] == "DevOpsFlow"
    assert response.json["version"] == "test"
    assert "/health" in response.json["endpoints"]


def test_health_probe_is_healthy():
    response = create_app({"TESTING": True}).test_client().get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_readiness_probe_is_ready():
    response = create_app({"TESTING": True}).test_client().get("/ready")

    assert response.status_code == 200
    assert response.json == {"status": "ready"}


def test_unknown_route_returns_json_404():
    response = create_app({"TESTING": True}).test_client().get("/missing")

    assert response.status_code == 404
    assert response.json == {"error": "Not found"}
