# Use the TensorFlow base image
FROM tensorflow/tensorflow:latest

# Set working directory
WORKDIR /app

# Install FastAPI, Uvicorn, and Optuna
RUN pip install fastapi==0.70.0 uvicorn==0.15.0 optuna==3.6.1
RUN pip install pydantic==1.10.2