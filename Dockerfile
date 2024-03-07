# Use the official Python image as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world
EXPOSE 8000

# Run FastAPI application
CMD ["bash", "-c", "python run_spider.py & uvicorn main:app --host 0.0.0.0 --port 8000"]
