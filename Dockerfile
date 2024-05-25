FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

EXPOSE 5000

# Command to run the Flask server
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]