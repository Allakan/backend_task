FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY . .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt
