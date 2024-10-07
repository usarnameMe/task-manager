# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY task_manager .

# Install any dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port Django will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
