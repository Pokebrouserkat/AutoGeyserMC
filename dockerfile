# Use a base image with Python and Java
FROM openjdk:23-slim

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory (can also be used as a volume mount point)
WORKDIR /app

# Copy your script into the image
COPY autoserver.py .

# Default command (you can override this in docker-compose or `docker run`)
CMD ["python3", "autoserver.py"]

# Expose the Java server port
EXPOSE 25565
# Expose the Bedrock server port
EXPOSE 19132
