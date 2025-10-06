# Use a lightweight Python image
FROM python:3.11-slim
LABEL authors="Johannes Theissen-Lipp"

# Set working directory
WORKDIR /app

# Copy requirements (optional, but flexible)
COPY requirements.txt ./

# Install dependencies (just pandas for this script)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY preprocess.py .

# Default command
CMD ["python", "preprocess.py"]
