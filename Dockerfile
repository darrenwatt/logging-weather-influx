FROM alpine
RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN pip3 install --no-cache-dir --upgrade pip
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY ./ /app

RUN rm -rf /var/cache/* 
RUN rm -rf /root/.cache/* 

ENV UID=1000
ENV GID=1000
RUN addgroup -g ${GID} -S appgroup && adduser -u ${UID} -S appuser -G appgroup
USER appuser

ENTRYPOINT [ "python3", "-u", "/app/main.py"]
LABEL maintainer=thedarrenwatt@gmail.com
