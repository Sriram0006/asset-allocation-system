FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy everything from the local 'app' folder into the container's '/app'
COPY ./app /app
# Copy the tests folder into the container
COPY ./tests /app/tests
EXPOSE 5000
CMD ["python", "main.py"]