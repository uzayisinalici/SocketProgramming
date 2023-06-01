import socket
import threading
import random
import time

class ClientHandler(threading.Thread):
    def __init__(self, client_socket, client_address):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.is_running = False

    def run(self):
        self.is_running = True
        print(f"New client connected: {self.client_address}")
        while self.is_running:
            data = self.client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received data from client {self.client_address}: {data}")

        self.client_socket.close()
        print(f"Client {self.client_address} disconnected.")

    def stop(self):
        self.is_running = False

class Server:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_handlers = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            client_handler = ClientHandler(client_socket, client_address)
            client_handler.start()
            self.client_handlers.append(client_handler)

    def stop(self):
        for client_handler in self.client_handlers:
            client_handler.stop()

        self.server_socket.close()
        print("Server stopped.")

if __name__ == "__main__":
    server = Server()
    server.start()
