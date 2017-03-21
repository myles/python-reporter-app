"""Python Report App Library."""
import logging
from logging import NullHandler

from .api import ReporterApp  # NOQA F401

__all__ = ['ReporterApp', '__version__', '__url__']

__version__ = '0.1.0'
__url__ = 'https://github.com/myles/python-reporter-app'

logging.getLogger(__name__).addHandler(NullHandler())
