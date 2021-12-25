FROM python:3.10.0
ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

COPY main.py handler.py config.py ./
EXPOSE 80

ENTRYPOINT [ "python", "main.py" ]
