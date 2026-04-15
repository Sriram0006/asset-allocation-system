FROM python:3.10-slim
WORKDIR /app
# Copy requirements from root to the image
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the entire app folder into the image
COPY . .
EXPOSE 5000
# Run the application
CMD ["python", "app/main.py"]