from setuptools import find_packages, setup

setup(
    name="project_atproto_dashboard",
    packages=find_packages(exclude=["project_atproto_dashboard_tests"]),
    install_requires=[
        "dagster==1.10.9",
        "dagster-aws",
        "dagster-dbt",
        "dagster-duckdb",
        "dagster-powerbi",
        "dbt-duckdb",
        "tenacity",
        "atproto",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest", "ruff"]},
)
