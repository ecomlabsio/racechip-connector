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
            logging.info(f"Successfully fetched {len(manufacturers)} manufacturers")
            return manufacturers
        except ValueError as e:
            logging.error(f"Error parsing JSON: {e}")
            return []
    else:
        logging.error(f"Failed to fetch manufacturers: HTTP {response.status_code}")
        return []

def main():
    logging.info("Starting to fetch RaceChip product data")
    manufacturers = fetch_manufacturers()

    if manufacturers:
        logging.info(f"Example manufacturer data: {manufacturers[0]}")
    else:
        logging.error("No manufacturers data fetched. Exiting.")
        return

    all_data = []

    for manufacturer in manufacturers:
        # Ensure the manufacturer data is accessed correctly.
        # Add an explicit check here to handle unexpected data structures.
        if isinstance(manufacturer, dict) and 'name' in manufacturer and 'id' in manufacturer:
            all_data.append({'Manufacturer': manufacturer['name'], 'Manufacturer ID': manufacturer['id']})
        else:
            logging.warning(f"Unexpected data structure for manufacturer: {manufacturer}")

    # Convert list to DataFrame
    df = pd.DataFrame(all_data)

    # Save to CSV
    df.to_csv('racechip_products.csv', index=False)
    logging.info("Data fetching complete and saved to racechip_products.csv")

if __name__ == "__main__":
    main()
