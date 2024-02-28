# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in Docker
WORKDIR /usr/src/app

# Install Poetry
RUN pip install poetry

# Copy the poetry.lock and pyproject.toml files to the container
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

# Copy the project files to the container
COPY ./src .

# Run the application when the container launches
CMD ["poetry", "run", "python", "server.py"]
