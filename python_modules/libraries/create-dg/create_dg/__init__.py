from dagster_shared.libraries import DagsterLibraryRegistry

from create_dg.version import __version__ as __version__

DagsterLibraryRegistry.register("create-dg", __version__)
