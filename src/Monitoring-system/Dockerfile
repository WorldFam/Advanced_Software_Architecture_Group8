FROM python:3.12.0

COPY . /

RUN pip3 install pymongo
RUN pip3 install python-dotenv
RUN pip3 install uvicorn
RUN pip3 install fastapi

CMD uvicorn main:app --host 0.0.0.0 --port 80