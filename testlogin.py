import subprocess
import requests
from bs4 import BeautifulSoup
import time
from tokenapi import get_token

# Run tokenapi.py to get the token
token = get_token()

# Save the token to a file (optional)
with open("token.txt", "w") as file:
    file.write(token)

# Read username and password from logpass.txt
with open("logpass.txt", "r") as file:
    lines = file.readlines()
    login_username = lines[0].strip()
    login_password = lines[1].strip()

# Set the URL for login
login_url = "https://tinychat.com/login"

# Set the headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Host": "tinychat.com",
    "Origin": "https://tinychat.com",
    "Referer": "https://tinychat.com/start?",
    "Upgrade-Insecure-Requests": "1",
}

# Create a session to handle cookies
session = requests.Session()

# Function to extract token from the login page
def extract_token(login_page_content):
    soup = BeautifulSoup(login_page_content, "html.parser")
    token_input = soup.find("input", {"name": "_token"})
    if token_input:
        return token_input["value"]
    return None

# Load the login page to extract the token
login_page_response = session.get(login_url)
token = extract_token(login_page_response.content)

# Set the payload data for login
payload = {
    "login_username": login_username,
    "login_password": login_password,
    "remember": "1",
    "next": "",
    "_token": token,
}

# Perform the login
response = session.post(login_url, headers=headers, data=payload, allow_redirects=False)

import subprocess
import requests
from bs4 import BeautifulSoup
import time
from tokenapi import get_token

# Run tokenapi.py to get the token
token = get_token()

# Save the token to a file (optional)
with open("token.txt", "w") as file:
    file.write(token)

# Read username and password from logpass.txt
with open("logpass.txt", "r") as file:
    lines = file.readlines()
    login_username = lines[0].strip()
    login_password = lines[1].strip()

# Set the URL for login
login_url = "https://tinychat.com/login"

# Set the headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Host": "tinychat.com",
    "Origin": "https://tinychat.com",
    "Referer": "https://tinychat.com/start?",
    "Upgrade-Insecure-Requests": "1",
}

# Create a session to handle cookies
session = requests.Session()

# Function to extract token from the login page
def extract_token(login_page_content):
    soup = BeautifulSoup(login_page_content, "html.parser")
    token_input = soup.find("input", {"name": "_token"})
    if token_input:
        return token_input["value"]
    return None

# Load the login page to extract the token
login_page_response = session.get(login_url)
token = extract_token(login_page_response.content)

# Set the payload data for login
payload = {
    "login_username": login_username,
    "login_password": login_password,
    "remember": "1",
    "next": "",
    "_token": token,
}

# Perform the login
response = session.post(login_url, headers=headers, data=payload, allow_redirects=False)

# Check if the login was successful (status code 302 indicates redirection)
if response.status_code == 302:
    print("Login successful")
    
    # Wait for 5 seconds before requesting API token...
    print("Waiting for 5 seconds before requesting API token...")
    time.sleep(5)
    
    # Use subprocess.Popen to run wss.py in the background
    subprocess.Popen(["python", "wss.py"])

    # You can print or use the response.headers to get additional information
    print("Headers:", response.headers)
else:
    print("Login failed. Status code:", response.status_code)
    print("Response content:", response.text)

