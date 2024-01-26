ARG PYTHON_VERSION=3.12.1
FROM python:${PYTHON_VERSION}-slim as base

# Set python environments
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
RUN --mount=type=bind,source=Pipfile,target=Pipfile \
    --mount=type=bind,source=Pipfile.lock,target=Pipfile.lock \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --ignore-pipfile --dev --system

# Copy the source code into the container.
COPY src/ src/

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["gunicorn", \
    "-w", "1", \
    "--reload", \
    "-b", "0.0.0.0:8000", \
    "src.wsgi:application"]
