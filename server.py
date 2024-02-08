
import requests
    import logging
    
    # Configure logging
    logging.basicConfig(filename='sync_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Function to fetch data from RaceChip API
    def fetch_racechip_products():
        racechip_api_url = "https://www.racechip.de/api/products"
        racechip_api_key = "b1ddd97910d0c400a31b87cc534d24eb"
        try:
            response = requests.get(f"{racechip_api_url}?apikey={racechip_api_key}")
            response.raise_for_status()  # Raise an error for non-200 status codes
            return response.json()['products']  # Assuming 'products' is the key containing product list
        except requests.exceptions.RequestException as e:
            logging.error("Failed to fetch RaceChip products: %s", str(e))
            return None  # Return None to indicate failure
    
    # Function to compare and sync products with BigCommerce
    def sync_products():
        racechip_products = fetch_racechip_products()
        if racechip_products:
            for product in racechip_products:
                # Add code to sync products with BigCommerce
                # This can include mapping, creating, or updating products in BigCommerce
                # For demonstration, let's just log the product details
                logging.info("Syncing product: %s", product['model'])  # Change this to actual sync code
    
    # Function to start the synchronization process
    def start_sync():
        sync_products()
        logging.info("Product synchronization with BigCommerce has been completed!")
    
    # Call the start_sync function to begin synchronization
    start_sync()
