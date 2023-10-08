import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_products(client):
    response = client.get('/api/products')
    assert response.status_code == 200

def test_get_product(client):
    response = client.get('/api/products/1')
    assert response.status_code == 404

# Add more tests for other endpoints and functionality

if __name__ == '__main__':
    pytest.main()


