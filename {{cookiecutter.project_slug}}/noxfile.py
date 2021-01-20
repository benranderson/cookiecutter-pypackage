import nox

locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.7", "3.8", "3.9"])
def tests(session):
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest", "--cov", "{{ cookiecutter.project_slug }}")


@nox.session(python=["3.7", "3.8", "3.9"])
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-broken-line",
        "flake8-comprehensions",
        "flake8-isort",
    )
    session.run("flake8", *args)


@nox.session(python="3.9")
def safety(session):
    session.install("safety")
    session.run("safety", "check", "--file=requirements.txt", "--full-report")
