FROM python:alpine AS build

ENV TZ=Asia/Tehran

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /app

WORKDIR /app

ADD . /app

ADD requirements.txt /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps build-base gcc musl-dev postgresql-dev && \
 python3 -m pip install -r /app/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN chmod u+x entrypoint.sh

EXPOSE 8080

CMD sh 

ENTRYPOINT ["sh", "entrypoint.sh"]
