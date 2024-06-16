FROM python:3.11-slim

WORKDIR /server

COPY requirements.txt /server

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

RUN pip install pydantic[email] -i https://mirrors.aliyun.com/pypi/simple/

COPY app /server/

ENV FAST_DEV=dev
#FROM python:3.11
#
#COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
#COPY --from=builder /server /server
#WORKDIR /server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]