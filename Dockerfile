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