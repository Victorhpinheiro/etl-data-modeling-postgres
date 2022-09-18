# Project Objectives

The objectives of the projects are to apply Data concepts into a real world scenario where a range of concepts will be applied modern technologies, such as:
- Data Modeling
- ETL
- Code Quality (clean and usable)

In order to do that we will analize data for a made up startup called "Sparkfy" where we have data from song and data from log in json format and ingest it, transform it and load into a star schema in postgre desgin for fast queries, analoge to data warehouse.

Finally, we will insert these process data in a POSTGRE database where we can than query for useful insghits.
---
# How to run

- First run:
```sh
python create_tables.py
```
This will create the database.

- Second run:
```sh
python etl.py
```
This will process all the files inside the folder data.
---
# Files
### sql_queries.py
All the queries used in this project in order to organize and make easy the re-use.

### create_tables.py
This call the queries and connect to the database to drop all table created and create new ones with no data inside.

### etl.ipynb
This one go to the methods of analyse and process datas for one file of log and one file of song in order to try out the logic and apply queries and code.

### test.ipynb
Run a series of test in the database and in the queries to verify if the project do not have the erros predict on it.

### etl.py
Process all the data from the sorce, transform it and then proceed to load it in the postgre database.
---
# Database Design
The design of the database follow the star schema where we have a fact table that hold the information that is important to analyse and keep track of the insightful information. Then, we will have 4 dimensions tables that hold information about single entities that are relevant of the fact table. This way we can easly query the fact table with useful information.

### songplays (Fact table)

Columns:
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### users (Dimension table)

Columns:
user_id, first_name, last_name, gender, level

### songs (Dimension table)

Columns:
song_id, title, artist_id, year, duration

### artists (Dimension table)

Columns:
artist_id, name, location, latitude, longitude

### time (Dimension table)

Columns:
start_time, hour, day, week, month, year, weekday