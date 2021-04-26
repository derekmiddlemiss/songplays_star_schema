# Fact table

songplays: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

# Dimension tables:

users: user_id, first_name, last_name, gender, level

songs: song_id, title, artist_id, year, duration

artists: artist_id, name, location, latitude, longitude

time: start_time, hour, day, week, month, year, weekday
