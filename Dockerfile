FROM python:3.10

WORKDIR /App
COPY requirements.txt /App/
RUN pip3 install -r requirements.txt

COPY . /App
CMD python3 -m Linux
