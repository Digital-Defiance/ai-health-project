# Use the TensorFlow base image
FROM tensorflow/tensorflow:latest

# Set working directory
WORKDIR /app

# Install FastAPI and other dependencies
RUN pip install fastapi==0.70.0 uvicorn==0.15.0

# Copy the application code to the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
