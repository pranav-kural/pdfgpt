"""
Utility functions for file handling
"""
import os
import shutil
import requests

def clear_source_file_contents(file_path):
    """
    method to clear the contents of the source file
    :param file_path: path of the file
    """
    with open(file_path, "w") as f:
        f.write("")

# delete the source file
def delete_source_file(file_path):
    """
    method to delete the source file
    :param file_path: path of the file
    """
    if os.path.exists(file_path):
        os.remove(file_path)

def download_pdf(url, file_path):
    """
    method to download PDF from URL
    :param url: URL of PDF document
    """
    # Obtain response
    response = requests.get(url, stream=True, timeout=10)

    # Save the file
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
    else:
        print(f'Failed to download PDF. Status code: {response.status_code}')
