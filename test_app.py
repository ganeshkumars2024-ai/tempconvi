from app import app
import pytest

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Temperature Converter" in response.data

def test_celsius_to_fahrenheit_conversion():
    client = app.test_client()
    response = client.post("/c-to-f", data={"celsius": "0"})
    assert response.status_code == 200
    assert b"32.00" in response.data
