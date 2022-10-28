##FROM continuumio/miniconda3:4.7.12
FROM jupyter/pyspark-notebook:latest

ADD covid19_project ./covid19_project
ADD configs ./configs
ADD dependencies ./dependencies
ADD tests ./tests
ADD requirements.txt ./requirements.txt

RUN pip install -r requirements.txt