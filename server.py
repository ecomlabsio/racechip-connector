import requests

# RaceChip API details
racechip_api_url = "https://www.racechip.de/api/products"
racechip_api_key = "b1ddd97910d0c400a31b87cc534d24eb"

# BigCommerce API details
bigcommerce_api_url = "https://api.bigcommerce.com/stores/{store_hash}/v3/catalog/products"
bigcommerce_access_token = "your_bigcommerce_access_token"
store_hash = "your_store_hash"

def fetch_racechip_products():
    """Fetch products from RaceChip."""
    response = requests.get(f"{racechip_api_url}?apikey={racechip_api_key}")
    if response.status_code == 200:
        return response.json()['products']  # Assuming 'products' is the key containing product list
    else:
        print("Failed to fetch RaceChip products")
        return []

def create_bigcommerce_product(product_data):
    """Create a product in BigCommerce."""
    headers = {
        "X-Auth-Token": bigcommerce_access_token,
        "Content-Type": "application/json"
    }
    response = requests.post(bigcommerce_api_url.format(store_hash=store_hash), json=product_data, headers=headers)
    if response.status_code == 201:
        print("Product created successfully in BigCommerce")
    else:
        print("Failed to create product in BigCommerce")

def map_product_data(racechip_product):
    """Map RaceChip product data to BigCommerce format."""
    return {
        "name": racechip_product['model'],  # Assuming 'model' holds the product name
        "type": "physical",
        "weight": racechip_product.get('weight', 1),  # Providing a default weight
        "price": racechip_product['price'],
        "sku": racechip_product['partNumber'],  # Assuming 'partNumber' as SKU
        "categories": [12345],  # Example category ID, replace with actual ID
        "availability": "available",
        "inventory_level": 100,
    }

def main():
    racechip_products = fetch_racechip_products()
    for product in racechip_products:
        bigcommerce_product_data = map_product_data(product)
        create_bigcommerce_product(bigcommerce_product_data)

if __name__ == "__main__":
    main()