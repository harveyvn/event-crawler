# SNORLAX: Automatically Crawling Events with Python

This document describes how to install and use SNORLAX. A video demonstration of the tool is available on [YouTube](https://youtu.be/3FeCl4ayFvs).

## Goals
- Crawl events (date, time, location, title, artists, works and image link).
- Insert data into database (PostgresSQL), with a self-defined schema.
- Run on different machines with docker compose.
- Attractive interactive prompt python.
- Export database as csv file.

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

Waking Snorlax up and walk through interactive prompts.
```
docker-compose run --rm app && docker-compose down postgres
```
<p align="left"><img src="https://user-images.githubusercontent.com/3027146/150591255-90c347b8-0acc-4920-8694-bac3fb293364.jpg" width="600"></p>

Executing Tests and perform on-the-fly line coverage measuring for source code with low runtime overhead.
```
docker-compose run --rm test && docker-compose down postgres
```
<p align="left"><img src="https://user-images.githubusercontent.com/3027146/150591460-d9630c95-a0e9-4705-916d-19d649f99d7e.jpg" width="600"></p>
