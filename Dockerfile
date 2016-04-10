FROM python:3.5

#Install dependencies
RUN apt-get install libffi-dev libyaml-dev -y

#Add files
ADD . /wololobot
WORKDIR /wololobot

#Install PIP dependencies
RUN pip install -r requirements.txt

CMD python run.py