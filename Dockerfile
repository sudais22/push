FROM python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY rest2.py ./
COPY auth_user.py ./
COPY retrieve_stocks.py ./
EXPOSE 8888
CMD ["python", "rest2.py"]
