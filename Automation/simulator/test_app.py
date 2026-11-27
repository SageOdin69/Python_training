import threading
import time
import pytest
import xdist
from task1 import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_equipment(client):
    print("Testing GET /api/equipment")
    response = client.get('/api/equipment')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]['id'] == 101
    assert data[0]['name'] == "Flight Control Unit"
    assert data[0]['type'] == "FCV"
    assert data[0]['status'] == "Operational"
    assert data[1]['id'] == 102
    assert data[1]['name'] == "Navigation System"
    assert data[1]['type'] == "NAV"
    assert data[1]['status'] == "Operational"
    assert data[2]['id'] == 103
    assert data[2]['name'] == "Communication Array"
    assert data[2]['type'] == "COM"
    assert data[2]['status'] == "Under Maintenance"
    print("GET /api/equipment test passed")

@pytest.mark.parametrize("equipment_id", [101, 102, 103])
def test_get_equipment_by_id(client, equipment_id):
    print(f"Testing GET /api/equipment/{equipment_id}")
    response = client.get(f'/api/equipment/{equipment_id}')
    assert response.status_code == 200
    data = response.get_json()
    if (equipment_id == 101):
        print("Employee ID: ", data['id'])
        print("Name: ", data['name'])
        print("Type: ", data['type'])
        print("Status: ", data['status'])
    elif (equipment_id == 102):
        print("Employee ID: ", data['id'])
        print("Name: ", data['name'])
        print("Type: ", data['type'])
        print("Status: ", data['status'])
    print("GET /api/equipment/{equipment_id} test passed")
