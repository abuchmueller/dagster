from setuptools import find_packages, setup

setup(
    name="project_ask_ai_dagster",
    packages=find_packages(exclude=["project_ask_ai_dagster_tests"]),
    install_requires=[
        "langchain",
        "langchain-core",
        "gql",
        "python-dotenv",
        "langchain-community",
        "langchain-openai",
        "langchain-chroma",
        "dagster==1.10.9",
        "dagster-webserver",
        "dagster-openai",
        "dagster_duckdb",
        "chromadb",
        "tokenizers",
        "tenacity",
        "tqdm",
        "bs4",
        "lxml",
        "openai",
        "pinecone",
    ],
    extras_require={"dev": ["pytest", "ruff==0.8.4", "dagster-webserver"]},
)
