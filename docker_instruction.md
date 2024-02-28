Here's the updated `Dockerfile` for your project, with the `CMD` line adjusted to use the same command as specified in your README, including the `--reload` flag for development purposes:

```Dockerfile
# Use the official Python 3.9.6 image
FROM python:3.9.6
# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of your project to the working directory
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application with reload for development
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

To build your Docker image, use the following command in your terminal within the project directory:

```bash
docker build -t wordcountergpt-app .
```

After building the image, run your Docker container with a volume mapped to your project directory so that changes to files like `server.py` are reflected in real-time inside the container. Use this command:

```bash
docker run -d --name wordcountergpt-container -p 8000:8000 -v $(pwd):/app wordcountergpt-app
```

This command runs the Docker container in detached mode (`-d`), names it `wordcountergpt-container`, maps port 8000 on your host to port 8000 in the container, and mounts the current directory (`$(pwd)`) to `/app` inside the container. This setup facilitates development by allowing changes made to your project files to be automatically available inside the container.