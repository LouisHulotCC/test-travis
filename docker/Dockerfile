FROM python:3.7.4-buster

RUN mkdir /app

COPY requirements.txt /app/
COPY src/ /app/

WORKDIR /app

RUN pip3 install -e .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "-u", "main.py" ]
