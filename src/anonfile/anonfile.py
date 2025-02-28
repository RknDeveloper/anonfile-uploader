from .utils import upload_file, delete_file, login_anonfile
from urllib.parse import urlparse
import os
import requests
from .exceptions import AnonfileError

class Anonfile:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password      
        self.api_url = "https://www.anonfile.la/process/upload_file"
        self.login_url = "https://www.anonfile.la/process/login"
        self.delete_url = "https://www.anonfile.la/assets/include/process.php?task=delete_file"
        self.delete_file_url = "https://www.anonfile.la/process/delete_file"
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
    
    def login(self):
        return login_anonfile(self)
        
    def extract_file_id(self, file_link):     
        parsed_url = urlparse(file_link)
        path = parsed_url.path
        return os.path.basename(path)
        
    def upload_file(self, file_path, timeout=300):
        if self.email and self.password:
            self.login()
        return upload_file(self, file_path, timeout)

    def delete_file(self, files):
        if not self.email or not self.password:
            raise AnonfileError(f"Email & Password is required to delete files.")
        self.login()
        return delete_file(self, files)
