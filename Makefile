.PHONY: run test install clean docker-build docker-run

# Python interpreter
PYTHON = python3

# Flask application settings
FLASK_APP = src/app.py
FLASK_ENV = development

# Docker settings
DOCKER_IMAGE = join-the-siege
DOCKER_TAG = latest

# Run Flask development server
run:
	FLASK_APP=$(FLASK_APP) FLASK_ENV=$(FLASK_ENV) flask run

# Run tests
test:
	pytest -v tests/

# Run integration tests for openai_clf
test-integration:
	pytest -v tests/test_openai_clf.py

# Run unit tests (all tests except for openai_clf)
test-unit:
	pytest -v tests/ --ignore=tests/test_openai_clf.py

# Build Docker image
docker-build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run Docker container
docker-run:
	docker run -p 5000:5000 $(DOCKER_IMAGE):$(DOCKER_TAG)

# Clean Docker resources
docker-clean:
	docker rmi $(DOCKER_IMAGE):$(DOCKER_TAG)
