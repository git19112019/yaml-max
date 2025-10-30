"""Custom exceptions for LLMs_OS"""

class LLMsOSException(Exception):
    """Base exception for LLMs_OS"""
    pass

class ActionNotFoundError(LLMsOSException):
    """Action not found in registry"""
    pass

class ValidationError(LLMsOSException):
    """YAML validation error"""
    pass

class ExecutionError(LLMsOSException):
    """Action execution error"""
    pass
