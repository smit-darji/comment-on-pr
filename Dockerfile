FROM python:3.7.5-slim

RUN pip install PyGithub
# COPY entrypoint.py /entrypoint.py

# ENTRYPOINT python /entrypoint.py
COPY main.py /main.py
COPY file_name_validator.py /file_name_validator.py
COPY entrypoint.py /entrypoint.py
COPY github_actions.py /github_actions.py

ENTRYPOINT python /entrypoint.py