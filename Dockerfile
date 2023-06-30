FROM python:3.9

# Set the working directory
WORKDIR /app

# Install necessary packages for selenium
RUN apt-get update && apt-get install -yq \
    wget \
    curl \
    unzip \
    libgconf-2-4 \
    xvfb

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the entry point for the container
CMD ["python3", "main.py"]
