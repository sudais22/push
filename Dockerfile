
FROM python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY files  ./
EXPOSE 8888
CMD ["python", "rest2.py"]
