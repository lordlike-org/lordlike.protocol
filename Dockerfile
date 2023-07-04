FROM alpine:3.13
RUN apk add
WORKDIR /opt/lordlike_protocol
COPY requirements.txt ./
COPY protocol ./blog
ENV PYTHONPATH='/opt/lordlike_protocol'
EXPOSE 8000
ENTRYPOINT ['python3', 'manage.py']
CMD ['runserver']