FROM python:3.7
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
RUN chmod 600 /app/berta_telemqtt

CMD [ "python", "./main.py" ]