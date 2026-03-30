import pytest

async def test_register(client):
    response = await client.post("/api/v1/auth/register", json={
        "name": "Test Student",
        "email": "test@uni.edu",
        "password": "securepassword"
    })
    assert response.status_code == 200

async def test_login(client):
    pass
