FROM ubuntu:latest
LABEL maintainer="liebl@informatik.uni-leipzig.de"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	git \
	python3 \
	python3-pip \
	python3-dev \
	libtesseract-dev \
	libleptonica-dev \
	tesseract-ocr \
	tesseract-ocr-deu \
	tesseract-ocr-eng
#	r-base \
#	r-recommended
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# see https://community.rstudio.com/t/r-in-jupyter-under-linux/18594/4
#ADD add_r_kernel.sh /usr/local/bin/
#RUN chmod +x /usr/local/bin/add_r_kernel.sh && \ 
#    /usr/local/bin/add_r_kernel.sh

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_md && python3 -m spacy download de_core_news_md

EXPOSE 8888
RUN mkdir -p /work && chmod 777 /work && mkdir -p /home/jupyter && chmod 777 /home/jupyter

ARG JUPYTER_USER
RUN useradd -u ${JUPYTER_USER} jupyter
USER jupyter

CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --notebook-dir=/work --LabApp.token=''
