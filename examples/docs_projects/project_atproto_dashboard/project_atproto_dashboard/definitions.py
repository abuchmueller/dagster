import dagster as dg

# start_def
import project_atproto_dashboard.defs

defs = dg.Definitions.merge(
    dg.components.load_defs(project_atproto_dashboard.defs),
)
# end_def
