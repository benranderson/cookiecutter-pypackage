@echo off

SET 	match=re.match(r'^([a-zA-Z_-]+):.*?

IF /I "%1"==".DEFAULT_GOAL " GOTO .DEFAULT_GOAL
IF /I "%1"=="for line in sys.stdin" GOTO for line in sys.stdin
IF /I "%1"=="help" GOTO help
IF /I "%1"=="activate" GOTO activate
IF /I "%1"=="clean" GOTO clean
IF /I "%1"=="clean-build" GOTO clean-build
IF /I "%1"=="clean-pyc" GOTO clean-pyc
IF /I "%1"=="clean-test" GOTO clean-test
IF /I "%1"=="dev-install" GOTO dev-install
IF /I "%1"=="lint" GOTO lint
IF /I "%1"=="test" GOTO test
IF /I "%1"=="watch" GOTO watch
IF /I "%1"=="cover" GOTO cover
IF /I "%1"=="safe" GOTO safe
IF /I "%1"=="build" GOTO build
IF /I "%1"=="docs" GOTO docs
GOTO error

:.DEFAULT_GOAL
	CALL make.bat =
	CALL make.bat help
	GOTO :EOF

:for line in sys.stdin
	match = re.match(r'^([a-zA-Z_-]+):.*?
	if match:
	target, help = match.groups()
	print(f"{target:20} {help}")
	GOTO :EOF

:help
	@python -c "$$PRINT_HELP_PYSCRIPT" < %MAKEFILE_LIST%
	GOTO :EOF

:activate
	%userprofile%\.virtualenvs\{{ cookiecutter.dev_venv }}\Scripts\activate

:clean
	CALL make.bat clean-build
	CALL make.bat clean-pyc
	CALL make.bat clean-test
	GOTO :EOF

:clean-build
	RMDIR /Q /S build
	RMDIR /Q /S dist
	RMDIR /Q /S site
	RMDIR /Q /S .eggs
	DEL /S *.egg-info
	DEL /S *.egg
	GOTO :EOF

:clean-pyc
	DEL /S *.pyc
	DEL /S *.pyo
	DEL /S *~
	FOR /F %%i in ('DIR /S /B __pycache__*') DO RMDIR /Q /S %%i
	GOTO :EOF

:clean-test
	RMDIR /Q /S .tox
	RMDIR /Q /S .nox
	DEL /Q .coverage /F
	RMDIR /Q /S htmlcov
	DEL /Q cov.xml /F
	RMDIR /Q /S .pytest_cache
	DEL /Q .testmondata /F
	RMDIR /Q /S .hypothesis
	RMDIR /Q /S .ruff_cache
	GOTO :EOF

:dev-install
	CALL make.bat clean
	python -m pip install -e ".[dev]"
	GOTO :EOF

:lint
	ruff src tests
	GOTO :EOF

:test
	pytest tests
	GOTO :EOF

:watch
	ptw --runner "pytest --testmon tests"
	GOTO :EOF

:cover
	pytest tests --cov src --cov-report term --cov-report html
	htmlcov\index.html
	GOTO :EOF

:safe
    CALL make.bat clean
	safety check --full-report
    GOTO :EOF

:build
	python -m build
    GOTO :EOF

:docs
	sphinx-autobuild docs docs/_build/html --open-browser
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
