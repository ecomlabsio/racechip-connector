
import tkinter as tk
    from tkinter import messagebox
    import requests
    
    # Function to fetch data from RaceChip API
    def fetch_racechip_products():
        racechip_api_url = "https://www.racechip.de/api/products"
        racechip_api_key = "b1ddd97910d0c400a31b87cc534d24eb"
        response = requests.get(f"{racechip_api_url}?apikey={racechip_api_key}")
        if response.status_code == 200:
            return response.json()['products']  # Assuming 'products' is the key containing product list
        else:
            print("Failed to fetch RaceChip products")
            print("Status Code:", response.status_code)
            print("Response Content:", response.text)  # Print response content for debugging
            return None  # Return None to indicate failure
    
    # Function to compare and sync products with BigCommerce
    def sync_products():
        racechip_products = fetch_racechip_products()
        if racechip_products:
            for product in racechip_products:
                # Add code to sync products with BigCommerce
                # This can include mapping, creating, or updating products in BigCommerce
                # For demonstration, let's just print the product details
                print("Syncing product:", product['model'])  # Change this to actual sync code
    
    # Function to display a message box when the action is started
    def start_action():
        sync_products()
        messagebox.showinfo("Action Started", "Product synchronization with BigCommerce has been completed!")
    
    # Function to perform a check of the RaceChip database and display the result
    def perform_database_check():
        result = check_racechip_database()
        messagebox.showinfo("Database Check", f"RaceChip Database Status: {result}")
    
    # Create the main application window
    root = tk.Tk()
    root.title("RaceChip-BigCommerce Sync")
    
    # Create a button widget to start the action
    sync_button = tk.Button(root, text="Start Product Sync", command=start_action)
    sync_button.pack(pady=5)
    
    # Create a button widget to perform a database check
    check_button = tk.Button(root, text="Check RaceChip Database", command=perform_database_check)
    check_button.pack(pady=5)
    
    # Start the Tkinter event loop
    root.mainloop()
