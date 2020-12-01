FROM python:3.7
RUN apt update
RUN apt install python-pip -y 
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python3", "app.py"]
