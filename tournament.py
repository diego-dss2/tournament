#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from t_results")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from t_players")
    conn.commit()
    conn.close()    

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("select count(*) from t_players")
    q_players = c.fetchone()
    conn.close()
    return q_players[0]
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into t_players (name) values (%s) ", (name,))
    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("select a.id, a.name as player_name, " + 
              "(select count(*) from t_results b where b.id_winner = a.id) as wins, " + 
              "(select count(*) from t_results b where (b.id_winner = a.id) or (b.id_loser = a.id)) as matches " + 
              "from t_players a " + 
              "order by wins desc, name")
    #players = [{'id': int(row[0]), 'name': str(row[1]), 'wins': int(row[2]), 'matches': int(row[3])} for row in c.fetchall()]
    players = c.fetchall()
    conn.close()
    return players

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into t_results(id_winner, id_loser) values (%s, %s)", (winner, loser))
    conn.commit()
    conn.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # obtengo la lista de jugadores ordenada por cantidad de triunfos
    lista = playerStandings()
    # voy obteniendo de a dos para emparejarlos y que jueguen
    parejas = []
    for i in xrange(0,len(lista)-1, 2):
        parejas.append((lista[i][0], lista[i][1], lista[i+1][0], lista[i+1][1]))

    return parejas

