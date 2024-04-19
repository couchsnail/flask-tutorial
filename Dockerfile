FROM python
RUN pip install flask
RUN pip install yfinance
RUN pip install matplotlib
RUN pip install numpy

WORKDIR /flask-tutorial
COPY . .
EXPOSE 5000
ENV FLASK_APP=hello-render.py
CMD ["flask", "--app", "hello-render", "run"]