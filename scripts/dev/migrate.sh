#!/bin/bash

# Define the container name where your database is running
container_name="cine_book_api_container_dev"

# Execute Alembic upgrade command inside the Docker container
docker exec $container_name alembic upgrade head
