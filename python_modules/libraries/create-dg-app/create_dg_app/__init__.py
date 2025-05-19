from dagster_shared.libraries import DagsterLibraryRegistry

from create_dg_app.version import __version__ as __version__

DagsterLibraryRegistry.register("create-dg-app", __version__)
