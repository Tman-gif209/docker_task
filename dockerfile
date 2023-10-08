FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python compulsory_task.py