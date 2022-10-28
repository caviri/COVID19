##FROM continuumio/miniconda3:4.7.12
FROM jupyter/pyspark-notebook:latest

COPY covid19_project ./covid19_project
COPY configs ./configs
COPY dependencies ./dependencies
COPY tests ./tests
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt