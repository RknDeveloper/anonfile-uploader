from .utils import upload_file

class Anonfile:
    def __init__(self, domain="www.anonfile.la"):        
        self.domain = domain
    
    def upload_file(self, file_path):
        return upload_file(file_path, self.domain)
