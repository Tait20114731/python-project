# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:07:28 2024

@author: Tatenda Marimo 20114731
@description: Server program that listens for incoming connections on port 1234.
@version: 1.0
"""

import socket

#  Creates a server socket object using IPv4 and TCP protocol and binds the socket while puts the socket into listening mode.
def create_server_socket(host, port):
    # Create a socket object with IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created.")

    # Bind the socket to the host and port
    server_socket.bind((host, port))
    print(f"Socket bound to {host}:{port}")

    # Put the socket into listening mode
    server_socket.listen(5)
    print("Socket is now listening.")

    return server_socket

# Accepts incoming connections on the server socket.
def accept_connections(server_socket):
    try:
        while True:
            # Establish connection with client
            client_socket, client_address = server_socket.accept()
            print(f"Got connection from {client_address}")

            # Optional: Send a welcome message to the client
            welcome_message = "Thank you for connecting!\n"
            client_socket.send(welcome_message.encode('utf-8'))

            # Close the connection with the client
            client_socket.close()
            print(f"Connection with {client_address} closed.")
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed.")

def main():
    # Define host and port
    host = socket.gethostname()  
    port = 1234

    # Create and configure the server socket
    server_socket = create_server_socket(host, port)

    # Accept incoming connections
    accept_connections(server_socket)

if __name__ == '__main__':
    main()
