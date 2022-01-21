# SNORLER: Automatically Crawling Events with Python

This document describes how to install and use SNORLER. A video demonstration of the tool is available on [YouTube](https://google.com).

## Repo Organization

```
.
├── sql
│   └── create_tables.sql
├── snorlax
│   ├── modules
│   ├── tests
│   └── requirements.txt
└── docker-compose.yml
```
The `snorlax` folder contains the source code of the tool, including running code and unittest. 

`create_tables.sql` initializes necessary relations for later usage at the beginning.

`requirements.txt` lists the python packages needed to install the tool. They are in the usual format accepted by `pip`.

`docker-compose.yml` is a YAML file defining services: database, app running and test executing.

## Installation

Download the repository and execute those commands within the repository directory.

```
docker-compose build
```

Running Snorler and playing through interactive prompts.
```
docker-compose run --rm app && docker-compose down postgres
```



Executing Tests and review the code coverage.
```
docker-compose run --rm test && docker-compose down postgres
```
