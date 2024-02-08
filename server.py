import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# API key and base URL setup
API_KEY = 'b1ddd97910d0c400a31b87cc534d24eb'
BASE_URL = 'https://www.racechip.de/reseller_api/v3'

def fetch_manufacturers():
    url = f"{BASE_URL}/manufacturer?apikey={API_KEY}"
    logging.info(f"Fetching manufacturers from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        manufacturers = response.json()
        logging.info(f"Found {len(manufacturers)} manufacturers")
        return manufacturers
    else:
        logging.error(f"Failed to fetch manufacturers: {response.status_code}")
        return []

def fetch_models(manufacturer_id):
    url = f"{BASE_URL}/models?manufacturer_id={manufacturer_id}&apikey={API_KEY}"
    logging.info(f"Fetching models for manufacturer_id {manufacturer_id}")
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json()
        logging.info(f"Found {len(models)} models for manufacturer_id {manufacturer_id}")
        return models
    else:
        logging.error(f"Failed to fetch models for manufacturer_id {manufacturer_id}: {response.status_code}")
        return []

def main():
    logging.info("Starting to fetch RaceChip product data")
    manufacturers = fetch_manufacturers()
    all_data = []

    for manufacturer in manufacturers:
        # For simplicity, only manufacturer fetching is shown
        # Extend this loop to fetch models, motors, and products as needed
        all_data.append({'Manufacturer': manufacturer['name'], 'Manufacturer ID': manufacturer['id']})
        # Placeholder for additional fetching

    # Convert list to DataFrame
    df = pd.DataFrame(all_data)
    
    # Save to CSV
    df.to_csv('racechip_products.csv', index=False)
    logging.info("Data fetching complete and saved to racechip_products.csv")

if __name__ == "__main__":
    main()
