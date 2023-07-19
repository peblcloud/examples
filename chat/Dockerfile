FROM peblcloud/python:0.0.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app app
ENTRYPOINT python -u app/main.py
