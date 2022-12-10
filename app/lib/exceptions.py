"""
Into each program some exceptions must raise
"""

from typing import List, Optional


class ManagementAPIException(Exception):
    """
    Base exception class
    """


class MessageException(ManagementAPIException):
    """
    Exception class with a simple message
    """
    def __init__(self, message: str) -> None:  # pylint: disable=super-init-not-called
        self.message = message

    def __str__(self) -> str:
        return self.message


class ErrorListException(ManagementAPIException):
    def __init__(self, errors: List[str]) -> None:
        super().__init__()
        self.errors = errors

    def __str__(self) -> str:
        return ", ".join(self.errors)


class DeadlyException(MessageException):
    """
    Exceptions that kill the service
    """
    def __init__(self, message: str, exit_code: int) -> None:
        self.exit_code = exit_code
        super().__init__(message=message)


class ConfigException(DeadlyException):
    """
    Configuration Error
    """


class DoesNotExistException(MessageException):
    """
    The object / Document being searched for does not exist.
    """


class AlreadyExistsException(ManagementAPIException):
    """
    An object / Document already exists with this name / PK
    """


class NoBranchException(ManagementAPIException):
    """
    Couldn't determine the current Git branch.
    """


class DatabaseException(MessageException):
    """
    Something is wrong with the DB
    """


class CrudException(MessageException):
    """
    Create / Read / Update / Delete operation failed.
    """
    def __init__(self, message: str, http_return_code: int) -> None:
        self.http_return_code = http_return_code
        super().__init__(message=message)
