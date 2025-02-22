class AnofileError(Exception):
    """Base exception for Anonfile errors."""
    pass

class FileNotFoundError(AnofileError):
    """Exception raised when a file is not found."""
    pass

class TimeoutError(AnofileError):
    """Exception raised when the request times out."""
    pass

class ConnectionError(AnofileError):
    """Exception raised when there is a connection error."""
    pass
