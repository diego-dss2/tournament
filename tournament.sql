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
