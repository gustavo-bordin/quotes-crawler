FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt \
  && rm requirements.txt

COPY src/ .

CMD tail -f /dev/null