FROM python:3.9-alpine

WORKDIR /Project

ADD . /Project

RUN pip install -r requirements.txt

CMD ["python", "MainScores.py"]