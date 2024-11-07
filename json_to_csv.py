import requests
import pandas as pd

# URL of your JSON server (replace with your actual URL)
json_url = 'https://json-db-m5if.onrender.com/laptops'  # Example URL, replace with your server's endpoint

# Fetch data from the JSON server
response = requests.get(json_url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON data to a pandas DataFrame
    data = response.json()  # Get the JSON response
    df = pd.DataFrame(data)  # Convert to DataFrame
    
    # Save the DataFrame to a CSV file
    df.to_csv('laptop_data.csv', index=False)
    print("Data successfully converted to laptop_data.csv")
else:
    print(f"Failed to retrieve data from JSON server. Status code: {response.status_code}")
