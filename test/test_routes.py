import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200

# post new cart
def test_post_cart(client):
    cart_data = {
        "id": 1,
        "cart_id": 2,
        "cart": 3,
        "product_id": 4,
        "product": 5,
        "qty": 6,
        "item_price": 7,
    }

    response = client.post("/api/carts", json=cart_data)
    
    assert response.status_code == 201

    data = json.loads(response.data)

    assert "id" in data
    assert data["cart_id"] == cart_data["cart_id"]
    assert data["cart"] == cart_data["cart"]
    assert data["product_id"] == cart_data["product_id"]
    assert data["product"] == cart_data["product"]
    assert data["qty"] == cart_data["qty"]
    assert data["item_price"] == cart_data["item_price"]

    pass

