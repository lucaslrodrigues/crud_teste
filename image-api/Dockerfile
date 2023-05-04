FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["make","run-server"]