FROM python:3.8.10
RUN mkdir securepassword
WORKDIR /securepassword
ENV PYTHONUNBUFFERED=1
COPY .env .
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]