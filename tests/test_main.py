import importlib


def test_core_import_and_version():
    """Ensure the ``core`` package can be imported and exposes ``__version__``.

    The test validates both the import mechanism and that the version string
    matches the expected value defined in ``core.__init__``.
    """
    core = importlib.import_module('core')
    assert hasattr(core, '__version__'), "core module should have a __version__ attribute"
    assert core.__version__ == "1.0.0"
