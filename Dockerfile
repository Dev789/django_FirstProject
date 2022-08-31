#FROM python:3.9.9-alpine
#
#ENV PYTHONBUFFERED 1
#
#WORKDIR /dockertest/
#
#ADD requirements.txt /dockertest/
#
#RUN pip install -r requirements.txt
#
#ADD . /dockertest/
#
#EXPOSE 8000
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.9.9-alpine

ENV PYTHONNUNBUFFERED 1

WORKDIR /DockerTest

COPY requirements.txt /DockerTest/requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]

#EXPOSE 8000
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]