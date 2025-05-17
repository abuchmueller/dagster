from my_existing_project.assets import my_asset

import dagster as dg

defs = dg.Definitions(
    assets=[my_asset],
)
