FROM python:3.8

# Install pip requirements
COPY requirements.txt .
ADD server.py /
ADD client.py /
ADD resources /resources
RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "./server.py"]
