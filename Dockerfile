FROM python:3.7.5-slim

RUN pip install PyGithub
# COPY entrypoint.py /entrypoint.py

# ENTRYPOINT python /entrypoint.py
COPY main.py /main.py

ENTRYPOINT python /main.py