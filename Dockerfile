FROM python:3.11.3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV PYTHONPATH "${PYTHONPATH}:/code/app"

CMD ["uvicorn", "myproject.asgi:application", "--host", "0.0.0.0", "--port", "80"]