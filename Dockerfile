FROM   python:3.11.9-alpine3.19
LABEL  maintainer="the29a"

ENV GAK_USER gak
ENV TZ=Europe/Moscow
WORKDIR /home/gak


RUN apk update && \
  apk upgrade && \
  addgroup -S ${GAK_USER} && \
  adduser -S -G ${GAK_USER} ${GAK_USER} && \
  mkdir -p /home/${GAK_USER} && \
  chown ${GAK_USER}:${GAK_USER} /home/${GAK_USER}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


USER $GAK_USER
COPY --chown=${GAK_USER}:${GAK_USER} gak-sprayer.py ./gak-sprayer.py
ENTRYPOINT ["/usr/local/bin/python", "/home/gak/gak-sprayer.py"]
