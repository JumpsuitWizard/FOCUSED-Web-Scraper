# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory
WORKDIR /webapp

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

EXPOSE 4000
# Set the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000", "--debug"]
