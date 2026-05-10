from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_search_integration():
    response = client.get("/search?q=e90 petrol")

    assert response.status_code == 200
    data = response.json()

    assert "generations" in data
    assert "E90" in data["generations"]
    assert "engines" in data["generations"]["E90"]


def test_search_empty_query():
    response = client.get("/search?q=")

    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_too_short"


def test_search_case_insensitive():
    response = client.get("/search?q=E90 PeTrOl")

    assert response.status_code == 200
    data = response.json()

    assert "generations" in data
    assert "E90" in data["generations"]


def test_search_best_intent():
    response = client.get("/search?q=F30 best diesel")

    assert response.status_code == 200
    data = response.json()

    assert "generations" in data
    assert "F30" in data["generations"]

    f30 = data["generations"]["F30"]

    assert "best_engine" in f30
    assert f30["best_engine"] is not None

    assert "engines" in f30


def test_search_series_detection():
    response = client.get("/search?q=3 series petrol")

    assert response.status_code == 200
    data = response.json()

    assert "generations" in data
    assert any("3" in key or "F30" in key or "E90" in key for key in data["generations"])


def test_search_x_family():
    response = client.get("/search?q=X5 diesel")

    assert response.status_code == 200
    data = response.json()

    assert "generations" in data
    generations = data["generations"]
    assert len(generations) > 0
    expected_generations = ["E53", "E70", "F15", "G05"]
    assert any(gen in generations for gen in expected_generations)


def test_search_fallback_all():
    response = client.get("/search?q=unknown query")

    assert response.status_code == 200
    data = response.json()

    assert "message" in data
    assert data["message"] == "Please select series or model"