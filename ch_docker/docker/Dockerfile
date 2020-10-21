FROM ubuntu:latest
LABEL maintainer="liebl@informatik.uni-leipzig.de"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
	build-essential \
	git \
	python3 \
	python3-pip \
	libtesseract-dev \
	libleptonica-dev \
	tesseract-ocr \
	tesseract-ocr-deu \
	tesseract-ocr-eng
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_md && python3 -m spacy download de_core_news_md

EXPOSE 8888
RUN mkdir -p /work && mkdir -p /home/jupyter && chmod 777 /home/jupyter

RUN useradd -u 8877 jupyter
USER jupyter

CMD jupyter lab --ip=* --port=8888 --no-browser --notebook-dir=/work --LabApp.token=''
