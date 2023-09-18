import requests

# Define the base URL for the API
base_url = "https://api.chainabuse.com/v0/reports/batch"

# Merged list of dictionaries with unique project names
merged_list = [
    {'project_name': 'Kingfund Finance', 'date_of_attack': '01/21/2022', 'amount_lost': '234000'},
    {'project_name': 'AFKSystem', 'date_of_attack': '01/19/2022', 'amount_lost': '12000000'},
    {'project_name': 'Crypto.com', 'date_of_attack': '01/18/2022', 'amount_lost': '34000000'},
    # ... other merged entries ...
]

# List to store API responses
api_responses = []

# Iterate through the merged data and make API requests
for project_entry in merged_list:
    project_name = project_entry['project_name']
    date_of_attack = project_entry['date_of_attack']
    amount_lost = project_entry['amount_lost']

    # Define the payload for the API request
    payload = {
        "agreedToBeContactedData": {"agreed": True},
        "scamCategory": "RUG_PULL",
        "addresses": [{"domain": project_name}],
        "tokens": [{"tokenId": amount_lost}],
        "description": f"Attack on {project_name} on {date_of_attack}"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    try:
        # Make the API request
        response = requests.post(base_url, json=payload, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            api_response_data = response.json()
            api_responses.append(api_response_data)
        else:
            print(f"API request for {project_name} failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error making API request for {project_name}: {str(e)}")

# Process the API responses as needed
for i, response_data in enumerate(api_responses, start=1):
    print(f"API Response {i}: {response_data}")