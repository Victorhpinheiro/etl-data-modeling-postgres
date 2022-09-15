# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                        songplay_id INT PRIMARY KEY UNIQUE,
                        start_time DATE NOT NULL,
                        user_id INT NOT NULL,
                        level VARCHAR,
                        song_id INT NOT NULL,
                        artist_id INT NOT NULL,
                        session_id INT NOT NULL,
                        location VARCHAR,
                        user_agent VARCHAR);
                        """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                    user_id INT PRIMARY KEY UNIQUE,
                    first_name VARCHAR NOT NULL,
                    last_name VARCHAR NOT NULL,
                    gender VARCHAR,
                    level VARCHAR NOT NULL);
                    """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                    song_id INT PRIMARY KEY UNIQUE,
                    title VARCHAR NOT NULL,
                    year VARCHAR NOT NULL,
                    duration DECIMAL NOT NULL);
                    """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                    artist_id INT PRIMARY KEY UNIQUE,
                    name VARCHAR NOT NULL,
                    location VARCHAR NOT NULL,
                    latitude VARCHAR,
                    longitude VARCHAR);
                    """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                    start_time numeric,
                    hour INT,
                    day VARCHAR ,
                    week int,
                    month VARCHAR NOT NULL,
                    year INT,
                    weekday VARCHAR);
                    """)

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]