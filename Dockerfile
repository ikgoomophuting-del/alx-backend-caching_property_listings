# Base Image
FROM python:3.10-slim
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose Django port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

