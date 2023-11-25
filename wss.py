import json
import websocket
from colorama import Fore, Style

# Read the token and WebSocket details from the file
with open("wss_details.json", "r") as file:
    wss_details = json.load(file)

# Extract WebSocket details
token = wss_details["token"]
websocket_url = wss_details["endpoint"]

# Connect to the WebSocket
ws = websocket.create_connection(websocket_url)

# Function to send a JSON message to the WebSocket
def send_message(message):
    ws.send(json.dumps(message))

# Function to handle incoming messages
def handle_message(message):
    # Add your logic here to process different types of messages
    print(Fore.GREEN + "Received message: {}".format(json.dumps(message, indent=2)) + Style.RESET_ALL)

# Join the room on the WebSocket
join_message = {
    "tc": "join",
    "req": 1,
    "useragent": "tinychat-client-webrtc-undefined_linux x86_64-2.0.20-420",
    "token": token,
    "room": "cancers",
    "nick": ""
}
send_message(join_message)

# Main loop to listen for messages
while True:
    try:
        message = ws.recv()
        if not message:
            break

        # Parse the message as JSON
        message_data = json.loads(message)
        handle_message(message_data)

        # Respond to pings
        if message_data.get("tc") == "ping":
            send_message({"tc": "pong", "req": message_data.get("req")})
    except websocket.WebSocketConnectionClosedException:
        print("WebSocket connection closed.")
        break
    except Exception as e:
        print("Error:", e)

# Close the WebSocket connection
ws.close()

