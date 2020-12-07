FROM python:3.7
RUN apt update
RUN apt install python-pip -y 
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5001
ENTRYPOINT ["gunicorn", "--workers=4", "-b","0.0.0.0:5001","app:app"]
