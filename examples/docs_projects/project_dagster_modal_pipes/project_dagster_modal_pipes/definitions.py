"""Poll podcast feeds, and e-mail summaries.

USAGE

    Ensure the following environment variables have been set

        CLOUDFLARE_R2_API
        CLOUDFLARE_R2_ACCESS_KEY_ID
        CLOUDFLARE_R2_SECRET_ACCESS_KEY
        OPENAI_API_KEY
        GMAIL_USER
        GMAIL_APP_PASSWORD
        SUMMARY_RECIPIENT_EMAIL

    Run Dagster

        dagster dev

"""

import dagster as dg

import project_dagster_modal_pipes.defs

# start_def
defs = dg.Definitions.merge(
    dg.components.load_defs(project_dagster_modal_pipes.defs),
)
# end_def
