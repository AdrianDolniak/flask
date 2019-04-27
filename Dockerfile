FROM python:2.7

ARG APP_DIR=/usr/src/flask_hello_world

WORKDIR /temp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p $APP_DIR
ADD hello_world/ $APP_DIR/hello_world/
ADD main.py $APP_DIR

CMD PYTHONPATH=$PYTHONPATH:/usr/src/flask_hello_world \
<<<<<<< HEAD
FLASK_APP=hello_world flask run --host=0.0.0.0
=======
  FLASK_APP=hello_world flask run --host=0.0.0.0
>>>>>>> dbfb1a7c98e1c8db7f82387e3ef1d118733fcf54
