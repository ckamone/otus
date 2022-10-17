FROM python:3.9-buster
COPY . .
WORKDIR .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
