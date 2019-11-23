FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN groupadd -r shortener_group && useradd -rg shortener_group shortener_user
RUN mkdir shortener
WORKDIR /shortener

ADD requirements.txt /shortener/
RUN pip install -r requirements.txt
ADD . /shortener/

USER shortener_user
