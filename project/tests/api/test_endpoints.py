import requests

def test_api_health_check():
    response = requests.get("http://127.0.0.1:5000/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
