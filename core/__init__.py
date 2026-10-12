"""core package

Provides core metadata and utilities for the *autod* project.

The module is deliberately lightweight – it currently only exposes a
``__version__`` attribute but is structured to allow future expansion
without breaking the public interface.

The implementation follows modern Python 3.10+ conventions:

*   Full type annotations.
*   Explicit ``__all__`` to define the public API.
*   Defensive handling to ensure the package can be imported both as a
    top‑level ``core`` package and as ``autod.core`` (when the project is
    installed as a package).  This is achieved by registering the module
    under the ``core`` name in ``sys.modules`` if it is imported via the
    ``autod.core`` path.
"""

from __future__ import annotations

import sys
from types import ModuleType
from typing import Final

# Public version identifier – kept in sync with the package metadata.
__version__: Final[str] = "1.0.0"

# Define the public symbols of this package.
__all__: list[str] = ["__version__"]

# ---------------------------------------------------------------------------
# Compatibility shim
# ---------------------------------------------------------------------------
# When the project is installed as ``autod`` the core package lives at
# ``autod.core``.  Some external code (including the test suite) imports the
# package directly as ``core``.  To keep the import path stable we alias the
# module in ``sys.modules`` under the top‑level name if it is not already
# present.  This operation is safe because it merely adds an additional
# reference to the same module object.
# ---------------------------------------------------------------------------
if "core" not in sys.modules:
    # ``sys.modules[__name__]`` is the current module object (e.g.
    # ``autod.core`` when imported via the package).  By assigning it to the
    # ``core`` key we make ``import core`` resolve to the same object.
    sys.modules["core"] = sys.modules[__name__]

# The module does not expose any runtime side‑effects beyond the aliasing
# performed above.  Future core utilities can be added below while keeping
# the public API stable.
