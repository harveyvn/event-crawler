SET timezone = 'Europe/Zurich';

DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS covers;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS event_locations;
DROP TABLE IF EXISTS event_covers;
DROP TABLE IF EXISTS event_artists;
DROP TABLE IF EXISTS event_songs;

CREATE TABLE IF NOT EXISTS locations (
	id serial PRIMARY KEY,
	name VARCHAR (255) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS covers (
	id serial PRIMARY KEY,
	url VARCHAR (500) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS songs (
	id serial PRIMARY KEY,
	title VARCHAR (250) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS artists (
	id serial PRIMARY KEY,
	name VARCHAR (250) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS events (
	id serial PRIMARY KEY,
	title VARCHAR (250) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS event_locations (
    event_id INTEGER,
    location_id INTEGER,
    date TIMESTAMPTZ,
    PRIMARY KEY (event_id, location_id)
);
CREATE TABLE IF NOT EXISTS event_covers (
    event_id INTEGER,
    cover_id INTEGER,
    PRIMARY KEY (event_id, cover_id)
);
CREATE TABLE IF NOT EXISTS event_artists (
    event_id INTEGER,
    artist_id INTEGER,
    PRIMARY KEY (event_id, artist_id)
);
CREATE TABLE IF NOT EXISTS event_songs (
    event_id INTEGER,
    song_id INTEGER,
    PRIMARY KEY (event_id, song_id)
);