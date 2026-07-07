"""Route smoke tests."""
from __future__ import annotations


def test_dashboard(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "ConvertX" in r.text


def test_converter_page(client):
    r = client.get("/converter")
    assert r.status_code == 200
    assert "Converter Workspace" in r.text


def test_supported_units_page(client):
    r = client.get("/supported-units")
    assert r.status_code == 200
    assert "Length" in r.text


def test_convert_endpoint_returns_partial(client):
    r = client.post(
        "/converter/convert",
        data={
            "category": "length",
            "value": "1",
            "from_unit": "kilometer",
            "to_unit": "mile",
            "precision": "4",
        },
    )
    assert r.status_code == 200
    assert "0.6214" in r.text


def test_convert_endpoint_invalid_value(client):
    r = client.post(
        "/converter/convert",
        data={
            "category": "length",
            "value": "not-a-number",
            "from_unit": "meter",
            "to_unit": "foot",
            "precision": "4",
        },
    )
    assert r.status_code == 200
    assert "Couldn't convert" in r.text
