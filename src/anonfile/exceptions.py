class AnonfileError(Exception):
    """Base exception for Anonfile errors."""
    pass

class FileNotFoundError(AnonfileError):
    """Exception raised when a file is not found."""
    pass

class TimeoutError(AnonfileError):
    """Exception raised when the request times out."""
    pass

class ConnectionError(AnonfileError):
    """Exception raised when there is a connection error."""
    pass

class JsonDecodeError(AnonfileError):
    """Exception raised when there is a JsonDecode error."""
    pass
