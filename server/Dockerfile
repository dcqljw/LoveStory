FROM python:3.11-slim
#FROM python:3.11 as builder

WORKDIR /server

COPY requirements.txt /server

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

RUN pip install pydantic[email]

COPY app /server/

#FROM python:3.11
#
#COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
#COPY --from=builder /server /server
#WORKDIR /server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]