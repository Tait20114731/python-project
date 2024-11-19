# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:15:28 2024

@author: Tatenda Marimo 20114731
@description: Client program that connects to a server on port 1234.
@version: 1.0
"""

import socket

#  Creates a client socket object using IPv4 and TCP protocols.
def create_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client socket successfully created.")
    return client_socket

# Connects the client socket to the specified server.
def connect_to_server(client_socket, host, port):
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

# Receives data from the server.
def receive_data(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data from server: {data}")
    return data

# Closes the client socket connection.
def close_connection(client_socket):
    client_socket.close()
    print("Client socket closed.")

def main():
    # Define server host and port
    host = socket.gethostname()
    port = 1234

    # Create a client socket
    client_socket = create_client_socket()

    try:
        # Connect to the server
        connect_to_server(client_socket, host, port)

        # Receive data from the server
        receive_data(client_socket)
    finally:
        # Close the client socket
        close_connection(client_socket)

if __name__ == '__main__':
    main()
