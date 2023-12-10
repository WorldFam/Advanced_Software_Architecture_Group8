FROM python:3.9

COPY requirements.txt /locust/
WORKDIR /locust

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install locust

COPY mqtt_locustfile.py /locust

CMD ["locust", "-f", "mqtt_locustfile.py"]