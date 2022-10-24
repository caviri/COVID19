FROM continuumio/miniconda3:4.7.12

RUN mkdir /opt/SDSC/
ADD covid19_project /opt/SDSC/covid_project/

WORKDIR /opt/SDSC/
ENV PYTHONPATH /opt/SDSC
RUN python setup.py install