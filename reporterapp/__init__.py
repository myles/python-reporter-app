"""Python Report App Library."""
import logging
from logging import NullHandler

from .api import Reporter  # NOQA F401

__all__ = ['Reporter']

logging.getLogger(__name__).addHandler(NullHandler())
