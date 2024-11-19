# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:30:25 2024

@author: Tatenda Marimo
@description: Unit testing for pdf_assesment3 program. This module includes tests for each function,
ensuring PDFs can be merged, rotated, encrypted, and decrypted correctly.
@version: 1.0
"""

import unittest
import os
import PyPDF2

# Importing functions from pdf_assesment3.
from pdf_assesment3 import merge_pdfs, rotate_pdf, encrypt_pdf, decrypt_pdf

# Unit test class for pdf_assesment3 module functions.
class TestPdfAssessment3(unittest.TestCase):

    #Set up test environment before each test.
    def setUp(self):
        # Creating sample PDF files for testing
        self.pdf1 = 'test_pdf1.pdf'
        self.pdf2 = 'test_pdf2.pdf'
        self.output_merge = 'merged_test.pdf'
        self.output_rotated = 'rotated_test.pdf'
        self.output_encrypted = 'encrypted_test.pdf'
        self.output_decrypted = 'decrypted_test.pdf'
        self.password = 'Password1'

        # Create sample PDFs
        writer = PyPDF2.PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(self.pdf1, 'wb') as f:
            writer.write(f)

        writer = PyPDF2.PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(self.pdf2, 'wb') as f:
            writer.write(f)
    # Clean up after each test.
    def tearDown(self):
        files_to_remove = [
            self.pdf1, self.pdf2, self.output_merge,
            self.output_rotated, self.output_encrypted, self.output_decrypted
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)
    # Test merging multiple PDF files into one.
    def test_merge_pdfs(self):
        pdf_list = [self.pdf1, self.pdf2]
        merge_pdfs(pdf_list, self.output_merge)
        self.assertTrue(os.path.exists(self.output_merge), f"Output file {self.output_merge} does not exist.")
        
        # Verify the merged PDF has the correct number of pages
        reader = PyPDF2.PdfReader(self.output_merge)
        self.assertEqual(len(reader.pages), 2, "Merged PDF should have 2 pages.")

    # Test rotating a specific page in a PDF file.
    def test_rotate_pdf(self):
        rotate_pdf(self.pdf1, self.output_rotated, page_number=0, rotation=90)
        self.assertTrue(os.path.exists(self.output_rotated), f"Output file {self.output_rotated} does not exist.")
        
        # Verify the page rotation
        reader = PyPDF2.PdfReader(self.output_rotated)
        page = reader.pages[0]
        self.assertEqual(page.get('/Rotate'), 90, "Page rotation is not correct.")

    # Test encrypting a PDF file with a password.
    def test_encrypt_pdf(self):
        merge_pdfs([self.pdf1], self.output_merge)
        encrypt_pdf(self.output_merge, self.output_encrypted, self.password)
        self.assertTrue(os.path.exists(self.output_encrypted), f"Output file {self.output_encrypted} does not exist.")
        
        # Verify the PDF is encrypted
        reader = PyPDF2.PdfReader(self.output_encrypted)
        self.assertTrue(reader.is_encrypted, "PDF should be encrypted but it's not.")

    # Test decrypting an encrypted PDF file with a password.
    def test_decrypt_pdf(self):
        merge_pdfs([self.pdf1], self.output_merge)
        encrypt_pdf(self.output_merge, self.output_encrypted, self.password)
        decrypt_pdf(self.output_encrypted, self.output_decrypted, self.password)
        self.assertTrue(os.path.exists(self.output_decrypted), f"Output file {self.output_decrypted} does not exist.")
        
        # Verify the decrypted PDF is not encrypted
        reader = PyPDF2.PdfReader(self.output_decrypted)
        self.assertFalse(reader.is_encrypted, "PDF should be decrypted but it's still encrypted.")

        # Verify the content matches the original
        original_reader = PyPDF2.PdfReader(self.output_merge)
        self.assertEqual(len(reader.pages), len(original_reader.pages), "Decrypted PDF does not match the original in page count.")

if __name__ == '__main__':
    print("Present", __name__)
    unittest.main()
