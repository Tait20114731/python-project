# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:13:24 2024

@author: Tatenda Marimo 20114731
@description: Unit testing for client socket program.
@version: 1.0
"""
import unittest
from unittest import mock
import socket

from client_socket import create_client_socket, connect_to_server, receive_data, close_connection

class TestClientSocket(unittest.TestCase):
    def setUp(self):
        # Set up host and port for testing
        self.host = 'localhost'
        self.port = 1234

    # Test that create_client_socket returns a socket object with the correct family and type.
    def test_create_client_socket(self):
        client_sock = create_client_socket()
        self.assertIsInstance(client_sock, socket.socket)
        self.assertEqual(client_sock.family, socket.AF_INET)
        self.assertEqual(client_sock.type, socket.SOCK_STREAM)
        client_sock.close()

    @mock.patch('client_socket.socket.socket.connect')
    def test_connect_to_server(self, mock_connect):
        
        #Test that connect_to_server calls the connect method with correct arguments.
        client_sock = create_client_socket()
        connect_to_server(client_sock, self.host, self.port)
        mock_connect.assert_called_with((self.host, self.port))
        client_sock.close()

    @mock.patch('client_socket.socket.socket.recv')
    def test_receive_data(self, mock_recv):
        
        #Test that receive_data correctly receives and decodes data from the server.
        client_sock = create_client_socket()
        # Mock the recv method to return predefined data
        mock_recv.return_value = b'Test data from server'
        data = receive_data(client_sock)
        self.assertEqual(data, 'Test data from server')
        client_sock.close()

    @mock.patch('client_socket.socket.socket.close')
    def test_close_connection(self, mock_close):
        
        #Test that close_connection calls the close method on the socket.
        client_sock = create_client_socket()
        close_connection(client_sock)
        mock_close.assert_called_once()

if __name__ == '__main__':
    print("Present", __name__)
    unittest.main()
