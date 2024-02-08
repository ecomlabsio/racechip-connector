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
        try:
            manufacturers = response.json()
            logging.info(f"Successfully fetched manufacturers")
            return manufacturers
        except ValueError as e:
            logging.error(f"Error parsing JSON: {e}")
            return {}
    else:
        logging.error(f"Failed to fetch manufacturers: HTTP {response.status_code}")
        return {}

def main():
    logging.info("Starting to fetch RaceChip product data")
    manufacturers = fetch_manufacturers()

    all_data = []

    for manufacturer_id, manufacturer_name in manufacturers.items():
        all_data.append({'Manufacturer ID': manufacturer_id, 'Manufacturer': manufacturer_name})

    # Convert list to DataFrame
    df = pd.DataFrame(all_data)

    # Save to CSV
    df.to_csv('racechip_products.csv', index=False)
    logging.info("Data fetching complete and saved to racechip_products.csv")

if __name__ == "__main__":
    main()
