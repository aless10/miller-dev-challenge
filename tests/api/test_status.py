def test_status_ok(app_client):
    response = app_client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"alive": True}
