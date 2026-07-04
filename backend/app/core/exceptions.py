"""
Application exceptions.
"""

from __future__ import annotations


class FlowForgeException(Exception):
    """Base exception."""


class ValidationException(FlowForgeException):
    """Validation error."""


class AuthenticationException(FlowForgeException):
    """Authentication error."""


class AuthorizationException(FlowForgeException):
    """Authorization error."""


class WorkflowException(FlowForgeException):
    """Workflow execution error."""


class ConfigurationException(FlowForgeException):
    """Configuration error.""" 