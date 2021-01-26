FROM python:3.8-slim-buster


WORKDIR /usr/src/Find-Your-Bike

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 5002

CMD ["python" "server.py"]


# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.8-slim-buster

# EXPOSE 5002

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

# WORKDIR /app
# COPY . /app

# # Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
# RUN useradd appuser && chown -R appuser /app
# USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# # CMD ["gunicorn", "--bind", "0.0.0.0:5002", "server\server:app"]

# CMD ["python" "server.py"]


