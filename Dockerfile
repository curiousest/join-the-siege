FROM python:3.12.0-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && \
    apt-get install -y tesseract-ocr

# Sync the project into a new environment, using the frozen lockfile
# TODO separate dev vs. prod dependencies
ADD pyproject.toml /app/
ADD .python-version /app/
ADD uv.lock /app/
WORKDIR /app
RUN uv sync --frozen
RUN uv pip install pip
RUN uv run spacy download en_core_web_sm
RUN uv pip install torch

# Copy the project into the image
ADD src/ /app/src/
ADD tests/ /app/tests/

ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production

# don't put secrets in the Dockerfile. This is just a placeholder.
ENV OPENAI_API_KEY=TODO
ENV PROJECT_ID=TODO

EXPOSE 5000

ENTRYPOINT ["uv", "run"]
CMD ["flask", "run", "--host=0.0.0.0"] 