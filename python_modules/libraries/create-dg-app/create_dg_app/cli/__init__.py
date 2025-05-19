import click
from dagster_dg.cli.scaffold import scaffold_project_command, scaffold_workspace_command
from dagster_dg.version import __version__

CREATE_DG_APP_CLI_MAX_OUTPUT_WIDTH = 120


def create_create_dg_app_cli():
    @click.group(
        name="create-dg-app",
        commands={
            "project": scaffold_project_command,
            "workspace": scaffold_workspace_command,
        },
        context_settings={
            "max_content_width": CREATE_DG_APP_CLI_MAX_OUTPUT_WIDTH,
            "help_option_names": ["-h", "--help"],
        },
    )
    @click.version_option(__version__, "--version", "-v")
    def group():
        """CLI for creating a new dg project or workspace."""

    return group


ENV_PREFIX = "CREATE_DG_APP"
cli = create_create_dg_app_cli()


def main():
    cli(auto_envvar_prefix=ENV_PREFIX)
