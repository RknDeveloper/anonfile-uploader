# Anonfile Uploader 
Anonfile Uploader is a simple Python library to upload files to [Anonfile.la](https://www.anonfile.la), including its temporary storage feature.

## Installation
```bash
pip install anonfile-uploader
```

## Use Without Login Example
```python
from anonfile import Anonfile

anonfile = Anonfile()
link = anonfile.upload_file('path/to/your/file.jpg')
print(f"Uploaded File: {link['url']}")
```

## Error Handling
The library comes with built-in exception handling to manage common errors such as timeouts, connection issues, or Json errors, others errors.
```python
from anonfile import Anonfile, TimeoutError, ConnectionError, JsonDecodeError, AnonfileError

uploader = Anonfile(email="your_email@example.com", password="your_password")
try:
    file_path = "path/to/your/file.txt"
    response = uploader.upload_file(file_path)
    print(f"Upload File: response['url']")
except TimeoutError:
    print("The upload took too long and timed out.")
except ConnectionError:
    print("Failed to connect to the server.")
except JsonDecodeError as e:
    print(f"Error: {str(e)}")
except AnonfileError as e:
    print(e)
```

## Handling Timeout
If the upload takes too long and exceeds the specified timeout, a TimeoutError will be raised.
```python
from anonfile import Anonfile, TimeoutError

uploader = Anonfile(email="your_email@example.com", password="your_password")
try:
    link = uploader.upload_file('path/to/your/file.jpg', timeout=10)
    print(f"Uploaded file: {link['url']}")
except TimeoutError:
    print("The upload took too long and timed out.")
```

## Handling Connection Issues
If there's a problem connecting to the anonfile.la , a ConnectionError will be raised.
```python
from anonfile import Anonfile, ConnectionError

uploader = Anonfile(email="your_email@example.com", password="your_password")
try:
    link = uploader.upload_file('path/to/your/file.jpg')
    print(f"Uploaded file: {link['url']}")
except ConnectionError:
    print("Failed to connect to the server.")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
