.PHONY: run test install clean

# Python interpreter
PYTHON = python3

# Flask application settings
FLASK_APP = src/app.py
FLASK_ENV = development

# Run Flask development server
run:
	FLASK_APP=$(FLASK_APP) FLASK_ENV=$(FLASK_ENV) flask run

# Run tests
test:
	pytest -v tests/
