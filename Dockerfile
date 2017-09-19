from ubuntu



RUN apt-get update
RUN apt-get install python-pip -y
RUN pip install --upgrade pip
RUN pip install PyGithub
