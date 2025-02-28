import requests
import os
import json
from .exceptions import AnonfileError, TimeoutError, ConnectionError, JsonDecodeError

def upload_file(self, file_path: str, timeout: int = 300) -> dict:
    """
    Upload a file to Anonfile.

    Args:
        file_path (str): Path to the file to upload.
        timeout (int, optional): Timeout for the upload request. Defaults to 300.

    Returns:
        dict: A dictionary containing the upload result.
            - success (bool): Whether the upload was successful.
            - url (str): The URL of the uploaded file.
            - message (str): A message describing the upload result.
            - is_image (bool): Whether the uploaded file is an image.

    Raises:
        AnonfileError: If upload fails.
        TimeoutError: If upload request times out.
        ConnectionError: If connection to Anonfile fails.
        JsonDecodeError: If JSON response is invalid.
        
    Example:
        Login:
            ```
            from anonfile import Anonfile

            anonfile = Anonfile(email="your_email@example.com", password="your_password")

            file_path = "path/to/your/file.txt"
            response = anonfile.upload_file(file_path)
            print("Upload File: ", response["url"])
            ```
        Not Login:
            ```
            from anonfile import Anonfile

           anonfile = Anonfile()

           file_path = "path/to/your/file.txt"
           response = anonfile.upload_file(file_path)
           print("Upload File: ", response["url"])
           ```
    """
    try:
        if isinstance(file_path, str):
            files = {'file': open(file_path, 'rb')}
        else:
            raise AnonfileError("Only file paths are supported in this version.")
            
        response = self.session.post(self.api_url, files=files, timeout=timeout)
        if response.status_code != 200 or not response.text:
            raise AnonfileError("Failed to upload file to Anonfile.")
            
        response.raise_for_status()
        response_data = response.json()
        
        if not response_data.get("success"):
            raise AnonfileError(response_data.get("message", "don't convert link."))
        return response_data
        
    except requests.exceptions.Timeout:
        raise TimeoutError(f"Upload request timed out after {timeout} seconds.")
    except json.JSONDecodeError as e:
        raise JsonDecodeError(f"Invalid response: {str(e)}")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Failed to connect to Anonfile.")
    except requests.exceptions.RequestException as e:
        raise AnonfileError(f"An error occurred: {str(e)}")

def delete_file(self, file_link: str) -> None:
    """
    Delete a file from Anonfile.

    Args:
        file_link (str): File link.

    Returns:
        None

    Raises:
        AnonfileError: If delete fails.
    
    Example:
        Login: # login required 
            ```
            from anonfile import Anonfile

           anonfile = Anonfile(email="your_email@example.com", password="your_password")

           file_link = "https://anonfile.com/your_file_id"
           response = anonfile.delete_file(file_link)
           print("Deleted File: ")
           ```
  
    """
    try:
        file_id = self.extract_file_id(file_link)
        data = {"file_link": file_id, "delete_file": "Delete"}
        delete_url = self.delete_url if "." in file_id else self.delete_file_url
        response = self.session.post(delete_url, data=data)
        
        if response.status_code != 200 or not response.text:
            raise AnonfileError("Failed to delete file to Anonfile.")
        response.raise_for_status()
        
        print("Deleted files: ", file_link)
    except requests.exceptions.RequestException as e:
        raise AnonfileError(f"Failed to delete files: {str(e)}")
        
def login_anonfile(self) -> None:
    """
    Login to Anonfile.

    Args:
        None

    Returns:
        None

    Raises:
        AnonfileError: If login fails.
    """
    try:
        login_data = {"email": self.email, "password": self.password, "login": "Login"}
        response = self.session.post(self.login_url, data=login_data)
        if response.status_code != 200 or not response.text:
            raise AnonfileError("Failed to login to Anonfile.")
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        raise AnonfileError(f"Failed to login: {str(e)}")
