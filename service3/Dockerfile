FROM python:3.7
RUN apt update
RUN apt install python-pip -y 
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5002
ENTRYPOINT ["gunicorn","--bind=0.0.0.0:5002", "app:app"]
