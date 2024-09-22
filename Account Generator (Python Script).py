import random
import string
import requests
import json

# Function to generate a random string
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate random account details (username, password)
def generate_account():
    username = generate_random_string(8)  # Random username (8 characters)
    password = generate_random_string(12)  # Random password (12 characters)
    return username, password

# Function to save account details to Google Sheets via Google Apps Script
def save_to_google_sheets(username, password):
    url = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE'  # Replace with your Google Apps Script URL

    data = {
        'username': username,
        'password': password
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print(f"Account saved: Username: {username}, Password: {password}")
        else:
            print(f"Failed to save account. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

# Main function to generate account and save it
def main():
    username, password = generate_account()
    save_to_google_sheets(username, password)

if __name__ == '__main__':
    main()
