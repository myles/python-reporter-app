"""Python Report App Library."""
import logging
from logging import NullHandler

from .api import ReporterApp  # NOQA F401
from ._meta import __version__, __project_name__  # NOQA F401

__all__ = ['ReporterApp', '__version__', '__project_name__']

logging.getLogger(__name__).addHandler(NullHandler())
