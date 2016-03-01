-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;
create database tournament;
\c tournament;

create table t_players(
    id serial,
    name text primary key
    );

create table t_results(
    id_result serial primary key,
    id_winner int,
    id_loser int
    );

create view v_player_standings as
    select
        a.id as player_id,
        a.name as player_name,
        (select count(*) from t_results b where b.id_winner = a.id) as wins,
        (select count(*) from t_results b where (b.id_winner = a.id) or (b.id_loser = a.id)) as matches
    from t_players a
