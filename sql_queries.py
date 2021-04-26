# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id INT PRIMARY KEY,
        start_time TIMESTAMP,
        user_id INT REFERENCES users(user_id),
        level VARCHAR,
        song_id VARCHAR REFERENCES songs(song_id),
        artist_id VARCHAR REFERENCES artists(artist_id),
        session_id INT,
        location VARCHAR,
        user_agent VARCHAR
    )
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        gender VARCHAR,
        level VARCHAR
    )
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR,
        artist_id VARCHAR REFERENCES artists(artist_id),
        year INT,
        duration REAL
    )
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id VARCHAR PRIMARY KEY,
        name VARCHAR,
        location VARCHAR,
        latitude REAL,
        longitude REAL        
    )
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INT GENERATED ALWAYS AS (EXTRACT(HOUR FROM start_time)) STORED,
        week INT GENERATED ALWAYS AS (EXTRACT(WEEK FROM start_time)) STORED,
        month INT GENERATED ALWAYS AS (EXTRACT(MONTH FROM start_time)) STORED,
        weekday VARCHAR GENERATED ALWAYS AS (EXTRACT(DOW FROM start_time)) STORED
    )
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

create_table_queries = [artist_table_create, song_table_create, user_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, time_table_drop, user_table_drop, song_table_drop, artist_table_drop]