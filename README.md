# Task 1: Visualization of COVID data

## Background

A common way of viewing statistics related to the COVID-19 pandemic has been dashboards. It led to the development of various data sources and programmatic ways of access. However, simply showing data without the underlying context may be misleading. Hence, bringing additional information that helps to understand and interpret data is critical. We would love to see your ideas for building pipelines that fetch data and relevant contextual information.

## Task

Set up a data processing and visualization pipeline for COVID data. You will retrieve the data from a public API (e.g., covidtracking.com), write code to process the data as needed, and provide visualizations of COVID infections over time.Thetask should:

- Allow interactive exploration and interpretation of covid infections in selected countries (e.g., US)
- Deliver a reproducible pipeline that re-executes automatically
- Provide a clean and well-documented code

## Format

Present your work in a well-documented repository, such as GitHub, GitLab, or RenkuLab.Resources

- Data API:https://covidtracking.com/data/api/version-2
- Create A Data Pipeline based on Messaging Using PySpark Hive:https://www.projectpro.io/project-use-case/build-a-data-pipeline-based-on-messaging-using-spark-and-hive

## Devnotes

They are gonna care about:

- Meaningful README
- FAIR principles (Findable, Accessible, Interoperable, Reusable)
- Reproducible research
- Good coding practices

### README

Here there should be information to understand what kind of data are we fetching. Information about how to deploy the app. What kind of dependencies are needed. Information about the coverage. A license. 

### FAIR

Docker container. Backup of the data requested. DOI in zenodo. A good documentation based on sphynx. Object orriented method so functions can be reused. 

### Reproducibility

Docker container. Heroku app. Unittest on the code. 

### Good coding practices

Type based programming. Tests. Inline documentation. Codestyle. Convention in the name of the variables. 

### Technologies

These technologies are mentioned on the pyproject page. 


- NiFi: Apache NiFi is a software project from the Apache Software Foundation designed to automate the flow of data between software systems. Real time streaming data import from external API using NiFi

- PySpark: Apache Spark is an open-source unified analytics engine for large-scale data processing. Spark provides an interface for programming clusters with implicit data parallelism and fault tolerance.

- HDFS:The Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It has many similarities with existing distributed file systems. However, the differences from other distributed file systems are significant. HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware. HDFS provides high throughput access to application data and is suitable for applications that have large data sets. 

- Kafka: Apache Kafka is a distributed event store and stream-processing platform. It is an open-source system developed by the Apache Software Foundation written in Java and Scala. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds

- Airflow: Apache Airflow is an open-source workflow management platform for data engineering pipelines

- Tableau: Tableau Software is an American interactive data visualization software company

- AWS QuickSight: Amazon QuickSight allows everyone in your organization to understand your data by asking questions in natural language, exploring through interactive dashboards, or automatically looking for patterns and outliers powered by machine learning.

- streamz: Streamz helps you build pipelines to manage continuous streams of data. It is simple to use in simple cases, but also supports complex pipelines that involve branching, joining, flow control, feedback, back pressure, and so on.


#### PySpark

PySpark is a great language for performing exploratory data analysis at scale, building machine learning pipelines, and creating ETLs for a data platform. If you’re already familiar with Python and libraries such as Pandas, then PySpark is a great language to learn in order to create more scalable analyses and pipelines.


#### Hive

Hive is an ETL and Data warehousing tool developed on top of the Hadoop Distributed File System. To begin with, in Hive, tables and databases could be created beforehand and then you can load data into them. 

### Database

The Covid Tracking Project: Data API. It contains 2 main categories: National Data, and State & Territories Data.  

#### National Data

- Historic US values: 
    - field_definitions
        - Total test results
        - Hospital discharges
        - Confirmed Cases
        - Cumulative hospitalized/Ever hospitalized
        - Cumulative in ICU/Ever in ICU
        - Cumulative on ventilator/Ever on ventilator
        - Currently hospitalized/Now hospitalized
        - Currently in ICU/Now in ICU
        - Currently on ventilator/Now on ventilator
        - Deaths (probable)
        - Deaths (confirmed)
        - Deaths (confirmed and probable)
        - Probable Cases
        - Last Update (ET)
        - New deaths
        - Date
        - States (**Non reported**)

Every field is organized in 3 categories: cases, testing, and outcomes. Then, every field can be accessed with aq dot after the category. 

- Single Day of data:
    - Same information but you don't need to download the whole dataset. This can be useful in order to make the dataretrieval parallel. 

#### State & Terrtories Data

- All state metadata: Basic information about all states, including notes about our methodology and the websites we use to check for data.
    - field_definitions
        - state_code
        - COVID Tracking Project preferred total test units
        - COVID Tracking Project preferred total test field
        - State population (2019 census)
        - Tertiary source for state COVID data
        - Secondary source for state COVID data
        - Primary source for state COVID data
        - FIPS code
        - State (or territory)

- Single State Metadata: Same but per state
    - field_definitions
        - state_code
        - COVID Tracking Project preferred total test units
        - COVID Tracking Project preferred total test field
        - State population (2019 census)
        - Tertiary source for state COVID data
        - Secondary source for state COVID data
        - Primary source for state COVID data
        - FIPS code
        - State (or territory)

- Historic data for a state or 
    - field_definitions
        - Total test results
        - Hospital discharges
        - Confirmed Cases
        - Cumulative hospitalized/Ever hospitalized
        - Cumulative in ICU/Ever in ICU
        - Cumulative on ventilator/Ever on ventilator
        - Currently hospitalized/Now hospitalized
        - Currently in ICU/Now in ICU
        - Currently on ventilator/Now on ventilator
        - Deaths (probable)
        - Deaths (confirmed)
        - Deaths (confirmed and probable)
        - Probable Cases
        - Last Update (ET)
        - New deaths
        - Date

- Single day of data for a state or territory
    - field_definitions
        - Total test results
        - Hospital discharges
        - Confirmed Cases
        - Cumulative hospitalized/Ever hospitalized
        - Cumulative in ICU/Ever in ICU
        - Cumulative on ventilator/Ever on ventilator
        - Currently hospitalized/Now hospitalized
        - Currently in ICU/Now in ICU
        - Currently on ventilator/Now on ventilator
        - Deaths (probable)
        - Deaths (confirmed)
        - Deaths (confirmed and probable)
        - Probable Cases
        - Last Update (ET)
        - New deaths
        - Date

### Day log

#### 23/10

Strategy A: Creating environment. 

- `python==3.9.13`
- PySpark uses java: `conda install openjdk==17.0.3`
- `conda install pyspark==3.3.0`
- `conda install ipykernel`
- `python -m ipykernel install --user --name covid19`


Strategy B: Docker machine

- `docker pull jupyter/pyspark-notebook`
- `docker run -p 10000:8888 jupyter/pyspark-notebook`


## License 

MIT License. 