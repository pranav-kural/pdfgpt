"""
Utility functions for file handling
"""
import os
import shutil
import requests

def clear_documents_directory():
    """
    method to clear documents directory
    """
    # clear documents directory
    if os.path.exists('data/documents'):
        shutil.rmtree('data/documents')
        os.makedirs('data/documents')
    else:
        os.makedirs('data/documents')

def download_pdf(url, file_path):
    """
    method to download PDF from URL
    :param url: URL of PDF document
    """
    # Obtain response
    response = requests.get(url)

    # Save the file
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
    else:
        print(f'Failed to download PDF. Status code: {response.status_code}')
