FROM r-base:latest

RUN apt-get update \
    && apt-get install -y python python-pip

COPY requirements.txt /usr/local/appfiles/
RUN pip install -r /usr/local/appfiles/requirements.txt

COPY . /usr/local/appfiles
WORKDIR /usr/local/appfiles

CMD ["python", "helloworld.py"]
