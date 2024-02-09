#!/bin/bash

# Define container name or ID
container_name="cine_book_api_container_dev"

# Default migration message
default_migration_message="Automatic database schema update"

# Parse command line arguments
while getopts ":m:" opt; do
  case ${opt} in
    m ) migration_message=$OPTARG;;
    \? ) echo "Usage: $0 [-m <migration_message>]"; exit 1;;
  esac
done

# If migration message is not provided, use the default message
if [ -z "$migration_message" ]; then
  migration_message="$default_migration_message"
fi

# Execute Alembic migration command inside the Docker container
docker exec $container_name alembic revision --autogenerate -m "$migration_message"
