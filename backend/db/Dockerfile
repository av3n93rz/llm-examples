FROM postgres:16

RUN apt-get update
RUN apt-mark hold locales
RUN apt-get install -y --no-install-recommends build-essential git postgresql-server-dev-16
RUN git config --global http.sslVerify false

RUN cd /tmp && \
  git clone --branch v0.6.0 https://github.com/pgvector/pgvector.git && \
  cd pgvector && \
  make clean && \
  make install