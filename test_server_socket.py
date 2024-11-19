# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:31:16 2024

@author: Tatenda Marimo 20114731
@description: Unit testing for server socket program.
@version: 1.0
"""

import unittest
from unittest import mock
import socket

from server_socket import create_server_socket, accept_connections

class TestServerSocket(unittest.TestCase):
    def setUp(self):
        # Define host and port for testing
        self.host = 'localhost'
        self.port = 1234

    @mock.patch('server_socket.socket.socket')
    def test_create_server_socket(self, mock_socket_class):
    
        #Test that create_server_socket creates a socket,
        #binds it to the correct address, and starts listening.
        mock_socket_instance = mock_socket_class.return_value

        # Call the function
        server_socket = create_server_socket(self.host, self.port)

        # Verify that socket.socket was called with AF_INET and SOCK_STREAM
        mock_socket_class.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)

        # Verify that bind was called with the correct host and port
        mock_socket_instance.bind.assert_called_with((self.host, self.port))

        # Verify that listen was called with the correct backlog
        mock_socket_instance.listen.assert_called_with(5)

        # Ensure the function returns the socket instance
        self.assertEqual(server_socket, mock_socket_instance)

    @mock.patch('server_socket.socket.socket')
    def test_accept_connections(self, mock_socket_class):
        
        # Test that accept_connections accepts incoming connections and handles them correctly.
        mock_server_socket = mock_socket_class.return_value
        mock_client_socket = mock.Mock()
        mock_client_address = ('127.0.0.1', 56789)
        
        # Configure accept method to return a client socket and address
        mock_server_socket.accept.return_value = (mock_client_socket, mock_client_address)
        
        # Set side effect to raise KeyboardInterrupt after first loop iteration
        def side_effect():
            # After the first accept call, raise KeyboardInterrupt to exit loop
            if not hasattr(side_effect, 'called'):
                side_effect.called = True
                return (mock_client_socket, mock_client_address)
            else:
                raise KeyboardInterrupt()
        mock_server_socket.accept.side_effect = side_effect

        # Mock the send and close methods on client socket
        mock_client_socket.send = mock.Mock()
        mock_client_socket.close = mock.Mock()
        
        # Call the function with the mocked server socket
        accept_connections(mock_server_socket)

        # Verify that accept was called
        self.assertTrue(mock_server_socket.accept.called, "Server did not accept any connections.")

        # Verify that send was called with the welcome message
        welcome_message = "Thank you for connecting!\n".encode('utf-8')
        mock_client_socket.send.assert_called_with(welcome_message)

        # Verify that client socket was closed
        mock_client_socket.close.assert_called_once()

        # Verify that server socket was closed in finally block
        mock_server_socket.close.assert_called_once()

if __name__ == '__main__':
    print("Present", __name__)
    unittest.main()
