# Use the base image you need
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy your application files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 8000:8000

# Run your Flask app
CMD ["python", "check.py"]
