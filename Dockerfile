FROM python:3.6

WORKDIR /usr/src/app

COPY try_dataclass_in_36.py .

CMD ["python", "try_dataclass_in_36.py"]