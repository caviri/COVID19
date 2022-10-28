Installation and run
====================

Installation
------------

Depdendencies can be installed using pip. 

.. code-block:: bash

    pip install -r requirements.txt

Run
---

In order to run the analysis we simply execute the python program. This will create a folder named ``output`` containing the parquet database and the final html with the interactive visualization. 

.. code-block:: bash

    python -m COVID19_project

Run tests
---------

Each transformation has its corresponding test. It is possible to run them with: 

.. code-block:: bash

    python -m unittest tests/test_*.py

Run in docker
-------------

It is possible to build a docker container from the dockerfile suministrated in the repository. This docker image is build uppon the jupyter-spark image and it comes with a jupyter lab interface. In order to build the image you can run: 

.. code-block:: bash

    docker build caviri/covid19:latest .

The in order to run the docker image you need to tunnel the ports. Jupyter uses ``8888`` port, and the pySpark UI uses ``4040`` ports. 

.. code-block:: bash

    docker run -p 10001:8888 -p 4041:4040 caviri/covid19

As an alternative to build your own image it is possible to pull a image from `docker hub <https://hub.docker.com/r/caviri/covid19>`__: 

.. code-block:: bash

    docker pull caviri/covid19:latest