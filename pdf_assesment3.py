# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:04:33 2024

@author: Tatenda Marimo 20114731
@description: Program that edits, merges, rotates, encrypt and decrypt PDF
files and saves those different versions of the files.
@version: 1.0
"""

import PyPDF2

# Merges multiple PDF files into one PDF file.
def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"PDF '{output_path}' merged successfully.")

# Rotates a specific page in a PDF file and saves it as a new PDF.
def rotate_pdf(input_pdf, output_pdf, page_number, rotation):

    # input_pdf: The input PDF file path.
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    num_pages = len(reader.pages)
    for i in range(num_pages):
        page = reader.pages[i]
        if i == page_number:
            page.rotate(rotation)
            # page_number: The page number to rotate.
            print(f"Page {page_number + 1} rotated by {rotation} degrees.")
        writer.add_page(page)
    #output_pdf: The output PDF file path.
    with open(output_pdf, 'wb') as outfile:
        writer.write(outfile)
    print(f"Rotated PDF saved as '{output_pdf}'.")

#Encrypts a PDF file with a password.
def encrypt_pdf(input_pdf, output_pdf, password):
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    # password: The password to encrypt the PDF.
    writer.encrypt(password)
    with open(output_pdf, 'wb') as outfile:
        writer.write(outfile)
    print(f"PDF '{input_pdf}' encrypted and saved as '{output_pdf}'.")
    

def decrypt_pdf(input_pdf, output_pdf, password):
    reader = PyPDF2.PdfReader(input_pdf)
    if reader.is_encrypted:
        try:
            reader.decrypt(password)
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)
            print(f"PDF file '{input_pdf}' decrypted and saved as '{output_pdf}'.")
        except Exception as e:
            print("Error decrypting PDF:", e)
    else:
        print(f"The PDF '{input_pdf}' is not encrypted.")


# Main function to execute PDF management tasks
def main():
   
    pdf_files = []
    num_files = int(input("Enter the number of PDF files to merge: "))
    for i in range(num_files):
        pdf_file = input(f"Enter the path for PDF file {i+1}: ")
        pdf_files.append(pdf_file)

    output_merge = 'merged.pdf'
    merge_pdfs(pdf_files, output_merge)

    #Rotate a page in PDF file
    input_pdf = 'test.pdf'  # Replace with your PDF filename
    output_rotated = 'rotated.pdf'
    page_num = 0  # Page number to rotate 
    rotation_angle = 90  # Rotation angle in degrees
    rotate_pdf(input_pdf, output_rotated, page_num, rotation_angle)

    #Encrypt PDF file
    input_pdf = 'merged.pdf'  # Replace with your PDF filename
    output_encrypted = 'encrypted.pdf'
    pwd = 'Password1'  # Password of encrypted files
    encrypt_pdf(input_pdf, output_encrypted, pwd)

    #Decrypt PDF file
    input_encrypted_pdf = 'encrypted.pdf'  # Encrypted PDF filename
    output_decrypted = 'decrypted.pdf'
    decrypt_pdf(input_encrypted_pdf, output_decrypted, pwd)

if __name__ == '__main__':
    main()
