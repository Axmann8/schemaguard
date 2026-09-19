"""Error types."""


class SchemaViolation(Exception):
    """Raised when a row does not satisfy the declared schema."""

    def __init__(self, message=""):
        super().__init__(message)
