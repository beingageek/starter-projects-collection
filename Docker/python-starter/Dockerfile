# Get latest image from docker hub
FROM python:3-slim

# Set working directory 
WORKDIR /usr/src/app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY . .

# Run Python app from command line
CMD ["python", "./python_test.py"]