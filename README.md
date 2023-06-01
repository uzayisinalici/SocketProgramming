# Server Code (server.py):
The Server class represents the server that listens for client connections and handles them.
The ClientHandler class is a thread that handles each connected client. It receives data from the client and prints it out.
When the server is started (start() method), it creates a server socket and binds it to the specified host and port.
The server enters a loop where it accepts incoming client connections using the accept() method. When a client connects, a new ClientHandler thread is created to handle that client.
The ClientHandler thread runs the run() method, which continuously receives data from the client using the recv() method. If the received data is empty, it indicates that the client has disconnected, and the thread terminates.
The server can be stopped by calling the stop() method, which stops all the ClientHandler threads and closes the server socket.

# Client Code (client.py):
The Client class represents the client that connects to the server and sends temperature data.
The connect() method establishes a connection to the server using the specified host and port.
The send_data() method sends the provided data to the server using the sendall() method.
The disconnect() method closes the client socket and disconnects from the server.
In the __main__ block, a Client object is created, and the client connects to the server using the connect() method.
The client enters an infinite loop where it generates random temperature data and sends it to the server using the send_data() method.
After sending the data, the client sleeps for 1 minute using time.sleep() to simulate the interval between data transmissions.
The loop continues indefinitely, and the client can be stopped by manually terminating the program or adding a condition to exit the loop.
Finally, the client disconnects from the server using the disconnect() method.
To run the code:

Start the server by running python server.py.
Run one or more instances of the client by executing python client.py.
