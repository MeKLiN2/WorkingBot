import time
import requests
import json

# Wait for 5 seconds
time.sleep(5)

def get_token():
    # Your existing logic to obtain the token
    # ...

    # For the purpose of this example, let's assume the token is obtained as follows:
    token = "b3ae169001fb5ee487ec3a361f7977647d8e3db1"

    return token

# Set the URL for the API request
api_url = "https://tinychat.com/api/v1.0/room/token/cancers"

# Set the headers for the API request
api_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Cookie": (
        "OptanonConsent=landingPath=NotLandingPage&datestamp=Fri+Nov+24+2023+16%3A41%3A25+GMT-0500+(Eastern+Standard+Time)"
        "&version=3.6.19&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1%2C0_13903%3A1%2C0_13902%3A1%2C101%3A1%2C102%3A1%2C103%3A1%2C"
        "104%3A1%2C105%3A1%2C106%3A1%2C107%3A1%2C108%3A1&AwaitingReconsent=false; "
        "_gcl_au=1.1.22349965.1700854636; "
        "XSRF-TOKEN=eyJpdiI6IjRkSWk1V2grUVpBWU9mWk1IaUFwOHc9PSIsInZhbHVlIjoieUhyVjBPWmRjbFZxczRXMHQ1bWZNWFBqUWlYYVVn"
        "aTRmaVRncFNtWktTK09pZzBFdENPVDJDaFVtWWpnU1lHQWNIRFE1ZG5pMWpUblJEaUFpZ2p2VXc9PSIsIm1hYyI6ImJkMjg4MzRiNzYyN"
        "2IzY2I0MTNlYjk2M2MwMmIxNmIzZjIyNjUwZTM4YTdjMGY1ZjMyODAzZGE5ODFhYThiM2UifQ==; "
        "tcsession=9192856780b85f205f2fdada7cd634d35c495436; "
        "sm_dapi_session=1; "
        "remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6Im1jc21xdTFoZGJtcDk5eFFNdkVLV1E9PSIsInZhbHVlIjoiMEY1S2VXR"
        "Wdkd2FpbHJ6YktDUFpGT3RTNmxqRDM0ZE54cjUweGtHM0FrbW5xaG9rOFJxTzU3TDdkaGp2NVNIWGdrbk9kbTdRTXZoelk0anlLNWxsQ"
        "zdyM29pMk5vbUhtWWd0M2tFbFpScnc9IiwibWFjIjoiZTRhYmJkMmFlZTUyZWFhZDA0MWNlNmJkNTk5NTVjZWQzNDU5NGE1OGM4ZGYwYj"
        "VhOTg2ZTEwMDlmNDU4NTFhNiJ9; "
        "hash=a545429f09eb77bc318d10daecca75ee; user=raise; pass=358e5a578a95f7a74da9caf99d09a3f4"
    ),
    "DNT": "1",
    "Host": "tinychat.com",
    "Referer": "https://tinychat.com/room/cancers",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
}

# Make the API request
api_response = requests.get(api_url, headers=api_headers)

# Print the API response content regardless of the status code
print("API Response Content:", api_response.text)

# Check if the API request was successful (status code 200)
if api_response.status_code == 200:
    try:
        # Attempt to decode the content as JSON
        api_data = api_response.json()
        print("API Token:", api_data.get("result"))
        print("API Endpoint:", api_data.get("endpoint"))

        # Save WebSocket details to a file
        wss_details = {
            "token": api_data.get("result"),
            "endpoint": api_data.get("endpoint")
        }

        with open("wss_details.json", "w") as file:
            json.dump(wss_details, file)
    except ValueError as ve:
        # Print the error message if JSON decoding fails
        print("Error parsing JSON:", ve)
    except Exception as e:
        # Print any other exceptions that may occur
        print("Error:", e)
else:
    print("API request failed. Status code:", api_response.status_code)

