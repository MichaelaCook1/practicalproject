FROM python:3.7
RUN apt update
RUN apt install python-pip -y 
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5003
ENTRYPOINT ["gunicorn", "--workers=4", "-b","0.0.0.0:5003","app:app"]
