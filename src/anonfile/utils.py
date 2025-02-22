import requests
import os
import json
from .exceptions import AnofileError, TimeoutError, ConnectionError

def upload_file(file_path, domain, timeout=30):
    """
    Uploads a file to Anonfile.

    Args:
        file_path (str): Path to the file to upload.
        domain (str): Domain of the Anonfile instance.
        timeout (int, optional): Timeout for the upload request. Defaults to 30.

    Returns:
        str: URL of the uploaded file.

    Raises:
        AnofileError: If the upload fails.
        TimeoutError: If the upload request times out.
        ConnectionError: If the connection to Anonfile fails.
        HTTPError: If an HTTP error occurs.
    """
    try:
        
        if isinstance(file_path, str):
            files = {'file': open(file_path, 'rb')}
        else:
            raise AnofileError("Only file paths are supported in this version.")

        response = requests.post(f"https://{domain}/process/upload_file", files=files, timeout=timeout)

        if response.status_code != 200 or not response.text:
            raise AnofileError("Failed to upload file to Anonfile.")

        return response.text.strip()

    except requests.exceptions.Timeout:
        raise TimeoutError(f"Upload request timed out after {timeout} seconds.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Failed to connect to Anonfile.")
    except requests.exceptions.RequestException as e:
        raise AnofileError(f"An error occurred: {str(e)}")
