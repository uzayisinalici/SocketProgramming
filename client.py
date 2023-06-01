import socket
import random
import time

class Client:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send_data(self, data):
        self.client_socket.sendall(data.encode())

    def disconnect(self):
        self.client_socket.close()
        print("Disconnected from server.")

if __name__ == "__main__":
    client = Client()
    client.connect()

    while True:
        # Generate random temperature data (replace with your own sensor data generation logic)
        temperature = random.uniform(0, 100)

        # Send temperature data to the server
        client.send_data(str(temperature))

        time.sleep(60)  # Sleep for 1 minute

    client.disconnect()
