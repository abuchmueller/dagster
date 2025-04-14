import dagster as dg

import project_ask_ai_dagster.defs

# start_def
defs = dg.components.load_defs(project_ask_ai_dagster.defs)
# end_def