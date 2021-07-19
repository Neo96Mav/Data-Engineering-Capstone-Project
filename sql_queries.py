# DROP TABLES
#This contains queries for dropping the tables that already exist
movies_table_drop = "DROP TABLE IF EXISTS Movies"
crew_table_drop = "DROP TABLE IF EXISTS Crew"
names_table_drop = "DROP TABLE IF EXISTS Names"
characters_table_drop = "DROP TABLE IF EXISTS Characters"
oscars_table_drop = "DROP TABLE IF EXISTS Oscars"
genres_table_drop = "DROP TABLE IF EXISTS Genres"
golden_globes_table_drop = "DROP TABLE IF EXISTS Golden_Globes"
votes_table_drop = "DROP TABLE IF EXISTS Votes"


# CREATE TABLES
#These queries are used to create the tables in our database 
#Movies is the fact-table and all the other tables are the dimension tables

movies_table_create = (""" 
CREATE TABLE IF NOT EXISTS Movies (
    imdb_title_id varchar PRIMARY KEY,
    title varchar NOT NULL,
    year int NOT NULL,
    duration int NOT NULL, 
    country varchar, 
    description varchar,
    metascore float,
    imdb_rating float,
    content_rating varchar, 
    tomatometer_status varchar, 
    tomatometer_rating float,
    audience_status varchar, 
    audience_rating float,
    num_oscars int,
    num_nominations_oscars int, 
    num_golden_globes int,
    num_nominations_globes int
    );""")

crew_table_create = (""" 
CREATE TABLE IF NOT EXISTS Crew(
    imdb_title_id varchar,
    ordering int,
    imdb_name_id varchar,
    category varchar,
    job varchar,
    PRIMARY KEY(imdb_title_id, imdb_name_id, category)
    );""")

names_table_create = (""" 
CREATE TABLE IF NOT EXISTS Names(
    imdb_name_id varchar PRIMARY KEY,
    name varchar NOT NULL,
    birth_name varchar NOT NULL, 
    height float,
    bio varchar, 
    birth_details varchar, 
    date_of_birth varchar, 
    place_of_birth varchar,
    death_details varchar, 
    date_of_death varchar,
    place_of_death varchar, 
    reason_of_death varchar
    );""")

characters_table_create = (""" 
CREATE TABLE IF NOT EXISTS Characters (
    imdb_title_id varchar,
    imdb_name_id varchar,
    category varchar,
    character varchar
    );""")

oscars_table_create = (""" 
CREATE TABLE IF NOT EXISTS Oscars (
    year int,
    year_ceremony int,
    ceremony int,
    category varchar, 
    name varchar, 
    title varchar, 
    winner bool, 
    imdb_title_id varchar,
    PRIMARY KEY(year, year_ceremony, ceremony, category, name, Title, winner)
    );""")

genres_table_create = (""" 
CREATE TABLE IF NOT EXISTS Genres (
    genre varchar,
    imdb_title_id varchar,
    PRIMARY KEY(Genre, imdb_title_id)
    );""")

golden_globes_table_create = (""" 
CREATE TABLE IF NOT EXISTS Golden_Globes (
    year int,
    year_award int,
    ceremony int ,
    category varchar, 
    nominee varchar, 
    title varchar, 
    win bool, 
    imdb_title_id varchar,
    PRIMARY KEY(year, year_award, ceremony, category, nominee, Title, win)
    );""")

votes_table_create = (""" 
CREATE TABLE IF NOT EXISTS Votes (
    imdb_title_id varchar PRIMARY KEY,
    imdb_votes float,
    rt_votes_critics float,
    rt_votes_audience float
    );""")

# INSERT RECORDS
#These queries are used to insert records into the tables. Though never used in the project, it is good to have these queries. 
movies_table_insert = (""" 
INSERT INTO Movies (
    imdb_title_id,
    Title,
    year,
    duration, 
    country, 
    description,
    metascore,
    IMDB_rating,
    content_rating, 
    tomatometer_status, 
    tomatometer_rating,
    audience_status, 
    audience_rating,
    num_oscars,
    num_nominations_oscars, 
    num_golden_globes,
    num_nominations_globes
    ) 
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (imdb_title_id)
DO 
    UPDATE SET (
    metascore,
    IMDB_rating,
    tomatometer_status, 
    tomatometer_rating,
    audience_status, 
    audience_rating,
    num_oscars,
    num_nominations_oscars, 
    num_golden_globes,
    num_nominations_globes) = 
    (EXCLUDED.metascore,
    EXCLUDED.IMDB_rating,
    EXCLUDED.tomatometer_status, 
    EXCLUDED.tomatometer_rating,
    EXCLUDED.audience_status, 
    EXCLUDED.audience_rating,
    EXCLUDED.num_oscars,
    EXCLUDED.num_nominations_oscars, 
    EXCLUDED.num_golden_globes,
    EXCLUDED.num_nominations_globes);
""")

crew_table_insert = (""" 
INSERT INTO Crew(
    imdb_title_id,
    ordering,
    imdb_name_id,
    category,
    job
    ) 
VALUES(%s, %s, %s, %s, %s)
""")

names_table_insert = (""" 
INSERT INTO Names (
    imdb_name_id,
    name,
    birth_name, 
    height,
    bio, 
    birth_details, 
    date_of_birth, 
    place_of_birth,
    death_details, 
    date_of_death,
    place_of_death, 
    reason_of_death
    ) 
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (imdb_name_id)
DO 
    UPDATE SET(
    death_details, 
    date_of_death,
    place_of_death, 
    reason_of_death) = 
    (EXCLUDED.death_details, 
    EXCLUDED.date_of_death,
    EXCLUDED.place_of_death, 
    EXCLUDED.reason_of_death);
""")

characters_table_insert = (""" 
INSERT INTO Characters (
    imdb_title_id,
    imdb_name_id,
    category,
    character
    ) 
VALUES(%s, %s, %s, %s)
""")


oscars_table_insert = (""" 
INSERT INTO Oscars (
    year,
    year_ceremony,
    ceremony,
    category, 
    name, 
    Title, 
    winner, 
    imdb_title_id
    ) 
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (year, year_ceremony, ceremony, category, name, Title, winner)
DO 
    UPDATE SET imdb_title_id = EXCLUDED.imdb_title_id;
""")

golden_globes_table_insert = (""" 
INSERT INTO Golden_Globes (
    year,
    year_award,
    ceremony,
    category, 
    nominee, 
    Title, 
    win, 
    imdb_title_id
    ) 
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (year, year_award, ceremony, category, nominee, Title, win)
DO 
    UPDATE SET imdb_title_id = EXCLUDED.imdb_title_id;
""")

genres_table_insert = (""" 
INSERT INTO Genres (
    Genre,
    imdb_title_id
    ) 
VALUES(%s, %s)
ON CONFLICT (Genre, imdb_title_id)
DO NOTHING;
""")

votes_table_insert = (""" 
INSERT INTO Votes (
    imdb_title_id,
    IMDB_votes,
    RT_votes_critics,
    RT_votes_audience
    ) 
VALUES(%s, %s, %s, %s)
ON CONFLICT (imdb_title_id) 
DO
    UPDATE SET (
    IMDB_votes,
    RT_votes_critics,
    RT_votes_audience)=
    (EXCLUDED.IMDB_votes,
    EXCLUDED.RT_votes_critics,
    EXCLUDED.RT_votes_audience);
""")

# QUERY LISTS

drop_table_queries = [movies_table_drop, crew_table_drop, names_table_drop, characters_table_drop, oscars_table_drop, genres_table_drop, golden_globes_table_drop, votes_table_drop]
create_table_queries = [movies_table_create, crew_table_create, names_table_create, characters_table_create, oscars_table_create, genres_table_create, golden_globes_table_create, votes_table_create]