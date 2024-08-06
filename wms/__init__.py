# -*- coding: utf-8 -*-
"""
    open-wms
    ~~~~~~~~


"""

from . import _version

__version__ = _version.get_versions().get("version")
del _version

from . import components  # noqa: F401

from . import system  # noqa: F401
from .system import System  # noqa: F401

from loris import Application  # noqa: F401


def load(name: str = "OpenWMS", factory=System, **kwargs) -> Application:
    return Application.load(name, factory=factory, **kwargs)
