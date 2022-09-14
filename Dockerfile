FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT 1

COPY . /usr/src/app
WORKDIR /usr/src/app



RUN pip install --upgrade pip
RUN pip install -U poetry
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
