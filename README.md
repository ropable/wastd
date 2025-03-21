# Western Australian Sea Turtles Database (WASTD)

This project is the Department of Biodiversity, Conservation and Attractions
Sea Turtles Database corporate application.

## Project layout / description

- `wastd`: the core Django project directory, containing common settings, configuration and templates.
- `observations`: the primary data model for the project, defining the `Encounter` and `Observation` models and subclasses.
- `users`: an extension of the Django `contrib.auth.models.User` class, customised for this project.
- `wamtram2`: auto-generated model classes to provide readonly ORM utility for the legacy WAMTRAM database.

The intent is for this project to replace the WAMTRAM legacy project and to act as the repository for
turtle tagging data. The `wamtram` application was created to ease access to the legacy database, and
the `tagging` application was created as an interim step to refactoring the legacy data into the
Encounter/Observation model defined in the `observations` application. It is expected that `wamtram` will
be removed after data migration, and that `tagging` will be removed after the data is refactored.

## Installation

This project uses [uv](https://docs.astral.sh/uv/) to manage and install Python dependencies.
With uv installed, install the required Python version (see `pyproject.toml`). Example:

    uv python install 3.12

Change into the project directory and run:

    uv python pin 3.12
    uv sync

Activate the virtualenv like so:

    source .venv/bin/activate

To run Python commands in the activated virtualenv, thereafter run them like so:

    python manage.py

Manage new or updated project dependencies with uv also, like so:

    uv add newpackage==1.0

## Environment variables

This project uses **python-dotenv** to set environment variables (in a `.env` file).
The following variables are required for the project to run:

    DATABASE_URL="postgis://USER:PASSWORD@HOST:5432/DATABASE_NAME"

Variables below may also need to be defined (context-dependent):

    SECRET_KEY=ThisIsASecretKey
    DEBUG=True
    GEOSERVER_URL=https://geoserver.url/service

## Running

Use `runserver` to run a local copy of the application:

    python manage.py runserver 0:8080

Run console commands manually:

    python manage.py shell_plus

## Media uploads

The production system stores media uploads in Azure blob storage.
Credentials for doing so should be defined in the following environment
variables:

    AZURE_ACCOUNT_NAME=name
    AZURE_ACCOUNT_KEY=key
    AZURE_CONTAINER=container_name

To bypass this and use local media storage (for development, etc.) simply set
the `LOCAL_MEDIA_STORAGE=True` environment variable and create a writable
`media` directory in the project directory.

## Docker image

To build a new Docker image from the `Dockerfile`:

    docker image build -t ghcr.io/dbca-wa/wastd .

## Docs

Use `sphinx-build` build docs locally:

    sphinx-build -b html docs _build

Use `http.server` serve them:

    python -m http.server --directory _build 8080

## Pre-commit hooks

This project includes the following pre-commit hooks:

- TruffleHog (credential scanning): <https://github.com/marketplace/actions/trufflehog-oss>

Pre-commit hooks may have additional system dependencies to run. Optionally
install pre-commit hooks locally like so:

    pre-commit install

Reference: <https://pre-commit.com/>
