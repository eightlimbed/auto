FROM python:3.6-alpine
LABEL app=auto_api
EXPOSE 5000
ENV DEBUG ""
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "/app/api.py"]
