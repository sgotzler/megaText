# code adopted from http://eeyore.ucdavis.edu/stat141/Hws/imdb.html

import sqlite3

# Connect to db

c = sqlite3.connect('imdb.db')
conn = c.cursor()

# build tables, set year range and kind_id

conn.execute('''
CREATE TABLE  title2 AS
SELECT * FROM title
 WHERE production_year >= 1940 AND production_year < 1960
   AND  (kind_id IN (2, 3, 5, 7));''')


conn.execute('''
CREATE TABLE  movie_keyword2 AS
  SELECT * FROM movie_keyword
   WHERE movie_id IN (SELECT id FROM title2);''')

conn.execute('''
CREATE TABLE  keyword2 AS
  SELECT * FROM keyword
   WHERE id IN (SELECT keyword_id FROM movie_keyword2);''')

conn.execute('''
CREATE TABLE  aka_title2 AS
  SELECT * FROM aka_title
   WHERE movie_id IN (SELECT id FROM title2);''')

conn.execute('''
CREATE TABLE  cast_info2 AS
  SELECT * FROM cast_info
   WHERE movie_id IN (SELECT id FROM title2);''')

conn.execute('''
CREATE TABLE  movie_info2 AS
  SELECT * FROM movie_info
   WHERE movie_id IN (SELECT id FROM title2);''')

conn.execute('''
CREATE TABLE  movie_info_idx2 AS
  SELECT * FROM movie_info_idx
   WHERE movie_id IN (SELECT id FROM title2);''')

conn.execute('''
CREATE TABLE  name2 AS
  SELECT * FROM name
   WHERE id IN (SELECT person_id FROM cast_info2);''')

conn.execute('''
CREATE TABLE  aka_name2 AS
  SELECT * FROM aka_name
   WHERE person_id IN (SELECT id FROM name2);''')

conn.execute('''
CREATE TABLE  person_info2 AS
  SELECT * FROM person_info
   WHERE person_id IN (SELECT id FROM name2);''')

conn.execute('''
CREATE TABLE movie_companies2 AS
  SELECT * FROM movie_companies
  WHERE movie_id IN (SELECT id FROM title2);''')

conn.execute('''
CREATE TABLE company_name2 AS
  SELECT * FROM company_name
  WHERE id IN (SELECT company_id FROM movie_companies2);''')

conn.execute('''
CREATE TABLE company_type2 AS
  SELECT * FROM company_type
  WHERE id IN (SELECT company_type_id FROM movie_companies2);''')

conn.execute('''
CREATE TABLE role_type2 AS
    SELECT * FROM role_type
    WHERE id IN (SELECT role_id FROM cast_info2);''')

conn.execute('''
CREATE TABLE char_name2 AS
    SELECT * FROM char_name
    WHERE id IN (SELECT person_role_id FROM cast_info2);''')

conn.execute('''
CREATE TABLE complete_cast2 AS
  SELECT * FROM complete_cast
  WHERE movie_id IN  (SELECT id FROM title2);''')

conn.execute('''
CREATE TABLE comp_cast_type2 AS
    SELECT * FROM comp_cast_type
    WHERE id IN  (SELECT status_id FROM complete_cast2);''')


#create indices

conn.execute('''
CREATE INDEX IF NOT EXISTS name_idx_name ON name2 (name);''')
conn.execute('''
CREATE INDEX name_idx_imdb_id ON name2 (imdb_id);''')
conn.execute('''
CREATE INDEX name_idx_pcodecf ON name2 (name_pcode_cf);''')
conn.execute('''
CREATE INDEX name_idx_pcodenf ON name2 (name_pcode_nf);''')
conn.execute('''
CREATE INDEX name_idx_pcode ON name2 (surname_pcode);''')
conn.execute('''
CREATE INDEX name_idx_md5 ON name2 (md5sum);''')
conn.execute('''
CREATE INDEX char_name_idx_name ON char_name2 (name);''')
conn.execute('''
CREATE INDEX char_name_idx_pcodenf ON char_name2 (name_pcode_nf);''')
conn.execute('''
CREATE INDEX char_name_idx_pcode ON char_name2 (surname_pcode);''')
conn.execute('''
CREATE INDEX char_name_idx_md5 ON char_name2 (md5sum);''')
conn.execute('''
CREATE INDEX company_name_idx_name ON company_name2 (name);''')
conn.execute('''
CREATE INDEX company_name_idx_pcodenf ON company_name2 (name_pcode_nf);''')
conn.execute('''
CREATE INDEX company_name_idx_pcodesf ON company_name2 (name_pcode_sf);''')
conn.execute('''
CREATE INDEX company_name_idx_md5 ON company_name2 (md5sum);''')
conn.execute('''
CREATE INDEX title_idx_title ON title2 (title);''')
conn.execute('''
CREATE INDEX title_idx_imdb_id ON title2 (imdb_id);''')
conn.execute('''
CREATE INDEX title_idx_pcode ON title2 (phonetic_code);''')
conn.execute('''
CREATE INDEX title_idx_epof ON title2 (episode_of_id);''')
conn.execute('''
CREATE INDEX title_idx_season_nr ON title2 (season_nr);''')
conn.execute('''
CREATE INDEX title_idx_episode_nr ON title2 (episode_nr);''')
conn.execute('''
CREATE INDEX title_idx_md5 ON title2 (md5sum);''')
conn.execute('''
CREATE INDEX aka_name_idx_person ON aka_name2 (person_id);''')
conn.execute('''
CREATE INDEX aka_name_idx_pcodecf ON aka_name2 (name_pcode_cf);''')
conn.execute('''
CREATE INDEX aka_name_idx_pcodenf ON aka_name2 (name_pcode_nf);''')
conn.execute('''
CREATE INDEX aka_name_idx_pcode ON aka_name2 (surname_pcode);''')
conn.execute('''
CREATE INDEX aka_name_idx_md5 ON aka_name2 (md5sum);''')
conn.execute('''
CREATE INDEX aka_title_idx_movieid ON aka_title2 (movie_id);''')
conn.execute('''
CREATE INDEX aka_title_idx_pcode ON aka_title2 (phonetic_code);''')
conn.execute('''
CREATE INDEX aka_title_idx_epof ON aka_title2 (episode_of_id);''')
conn.execute('''
CREATE INDEX aka_title_idx_md5 ON aka_title2 (md5sum);''')
conn.execute('''
CREATE INDEX cast_info_idx_pid ON cast_info2 (person_id);''')
conn.execute('''
CREATE INDEX cast_info_idx_mid ON cast_info2 (movie_id);''')
conn.execute('''
CREATE INDEX cast_info_idx_cid ON cast_info2 (person_role_id);''')
conn.execute('''
CREATE INDEX complete_cast_idx_mid ON complete_cast2 (movie_id);''')
conn.execute('''
CREATE INDEX keyword_idx_keyword ON keyword2 (keyword);''')
conn.execute('''
CREATE INDEX keyword_idx_pcode ON keyword2 (phonetic_code);''')
conn.execute('''
CREATE INDEX movie_keyword_idx_mid ON movie_keyword2 (movie_id);''')
conn.execute('''
CREATE INDEX movie_keyword_idx_keywordid ON movie_keyword2 (keyword_id);''')
conn.execute('''
CREATE INDEX movie_link_idx_mid ON movie_link2 (movie_id);''')
conn.execute('''
CREATE INDEX movie_info_idx_mid ON movie_info2 (movie_id);''')
conn.execute('''
CREATE INDEX movie_info_idx_idx_mid ON movie_info_idx2 (movie_id);''')
conn.execute('''
CREATE INDEX movie_info_idx_idx_infotypeid ON movie_info_idx2 (info_type_id);''')
conn.execute('''
CREATE INDEX movie_info_idx_idx_info ON movie_info_idx2 (info);''')
conn.execute('''
CREATE INDEX movie_companies_idx_mid ON movie_companies2 (movie_id);''')
conn.execute('''
CREATE INDEX movie_companies_idx_cid ON movie_companies2 (company_id);''')
conn.execute('''
CREATE INDEX person_info_idx_pid ON person_info2 (person_id);''')


# drop original tables

conn.execute('''
drop table if exists title;
''')

conn.execute('''
drop table if exists if exists person_info;
''')

conn.execute('''
drop table if exists aka_name;
''')

conn.execute('''
drop table if exists aka_title;
''')

conn.execute('''
drop table if exists movie_keyword;
''')

conn.execute('''
drop table if exists movie_info;
''')

conn.execute('''
drop table if exists movie_info_idx;
''')

conn.execute('''
drop table if exists keyword;
''')

conn.execute('''
drop table if exists cast_info;
''')

conn.execute('''
drop table if exists name;
''')

conn.execute('''
drop table if exists movie_companies;
''')

conn.execute('''
drop table if exists company_name;
''')

conn.execute('''
drop table if exists company_type;
''')

conn.execute('''
drop table if exists role_type;
''')

conn.execute('''
drop table if exists char_name;
''')

conn.execute('''
drop table if exists complete_cast;
''')

conn.execute('''
drop table if exists comp_cast_type;
''')

#execute all scripts

conn.execute('VACUUM')
conn.commit()
conn.close()
