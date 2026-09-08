"""Run with `uvx nox` (or `uv run nox`) - every session is built with uv."""

import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "tests"]

PYTHON = "3.12"


@nox.session(python=PYTHON)
def tests(session):
    """Run the pytest suite (Playwright end-to-end tests against the built widgets)."""
    session.install("-e", ".[test]")
    session.run("playwright", "install", "chromium")
    session.run("pytest", "tests", *session.posargs)


@nox.session(python=PYTHON)
def lint(session):
    """Run the pre-commit checks (ruff, formatting, prettier, ...) across the repo."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session(python=False)
def build_react(session):
    """Build the react-components bundle consumed by trame_mui.module."""
    with session.chdir("react-components"):
        session.run("npm", "ci", external=True)
        session.run("npm", "run", "lint", external=True)
        session.run("npm", "run", "build", external=True)
