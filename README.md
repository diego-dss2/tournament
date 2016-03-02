#Description#

This project consists in the development of a database schema to store the game results between players, and writing 
a Python script to rank them.


#Requirements#

In order to use this scripts you need:

* Python 2.x
* A working installation of PostgreSQL database


#Creating the database schema#

To create the database schema, follow these instructions:

* In the command line, navigate to the directory where the _tournament.sql_ file is located.
* Execute the following command from PostgreSQL command line:

 `\i tournament.sql`

#Running the test cases#

To run the test cases, execute the following command:

`python tournament_test.py`