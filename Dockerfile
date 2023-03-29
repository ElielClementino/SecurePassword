FROM python:3.8.10
RUN mkdir securepassword
WORKDIR /securepassword
ENV PYTHONUNBUFFERED=1
COPY .env .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
