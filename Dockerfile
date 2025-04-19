# Use official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and dependencies
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files to container
COPY . .

# Install required Python packages
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Run Flask application
CMD ["python3", "/app/app.py"]
