FROM alpine:3.13
RUN apk add
WORKDIR /opt/hello-world
COPY requirements.txt ./
COPY protocol ./blog
ENV PYTHONPATH='/opt/hello_world'
EXPOSE 8000
ENTRYPOINT ['python3', 'manage.py']
CMD ['runserver']