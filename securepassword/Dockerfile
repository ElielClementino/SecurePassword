FROM python:3.8.10
WORKDIR /securepassword
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT python manage.py runserver