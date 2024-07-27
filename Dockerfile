# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /app/
# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    # Cleanup
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app/

    # # Expose the port on which the Django app will run
# EXPOSE 8000

# # Run the Django app when the container starts
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
