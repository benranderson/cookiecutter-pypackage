import nox

locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.9", "3.10"])
def tests(session):
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest", "--cov", "{{ cookiecutter.project_slug }}")


@nox.session(python=["3.8", "3.9", "3.10"])
def lint(session):
    args = session.posargs or locations
    session.install("ruff")
    session.run("ruff", "check" * args)


@nox.session(python="3.10")
def safety(session):
    session.install("safety")
    session.run("safety", "check", "--file=requirements.txt", "--full-report")
