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

## License 

MIT License. 