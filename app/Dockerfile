# FROM python:3.11-slim

# WORKDIR /

# # COPY requirements.txt /app/
# COPY requirements.txt .

# # RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install -r requirements.txt

# # COPY . /app/
# COPY . .

# # COPY .env /app/  # Copy the .env file

# # EXPOSE 5000
# # CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
# CMD ["python", "app3.py"]

###################################

# FROM python:3.11-slim

# WORKDIR /app

# # COPY requirements.txt /app/
# COPY requirements.txt .

# # RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install -r requirements.txt

# # COPY . /app/
# COPY . .

# # COPY .env /app/  # Copy the .env file

# EXPOSE 80

# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]



##############################
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install gunicorn

COPY . .

# You might not need this line if your main file is not named "app3.py"
# CMD ["gunicorn", "app:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5000"]

# Make port XXXX available to the world outside this container
# EXPOSE 5000
# is more of a documentation feature, and it doesn't automatically publish the ports.

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# This flag sets the port on which Uvicorn will listen for incoming connections.

