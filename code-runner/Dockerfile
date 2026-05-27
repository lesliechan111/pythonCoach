FROM python:3.12-alpine

# Create a non-root user
RUN adduser -D -s /bin/sh runner

# Set working directory
WORKDIR /sandbox

# No network access, read-only root, limited resources
# The backend will spawn this container with:
#   --network none
#   --read-only
#   --memory=128m
#   --cpus=0.5
#   --pids-limit=50

USER runner

# Default: read code from stdin and execute
CMD ["python3", "-c", "import sys; exec(sys.stdin.read())"]
