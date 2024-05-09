FROM ubuntu
RUN apt update
RUN apt install -y python3-pip
RUN pip install flask
RUN pip install yfinance
RUN pip install matplotlib
RUN pip install numpy

WORKDIR /flask-tutorial
COPY . .
EXPOSE 5000
#ENV FLASK_APP=hello-render.py
CMD [ "flask", "--app", "hello-render.py", "run", "--host=0.0.0.0"]

# ENTRYPOINT [ "flask"]
# CMD [ "run", "--host", "0.0.0.0" ]
#ENTRYPOINT ["python3 hello-render.py"]