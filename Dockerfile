FROM continuumio/miniconda3

WORKDIR /home

EXPOSE 5000

COPY . .

RUN apt-get update && \
    apt-get install -y build-essential libgmp-dev libmpfr-dev

RUN pip install grpcio 


RUN pip install torch
RUN pip install torchvision

RUN pip install -r requirements.txt

CMD ["flask", "run"]