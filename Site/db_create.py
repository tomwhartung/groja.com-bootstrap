""" Create a sqlite3 db for the NameEmail table

Purpose: Create the db, create the table, seed in one row of data
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference (for Flask DB patterns):
  http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
Usage:
  Create the db and seed it with one row of data
    python3 -m db_create
    db_create.sh
"""

import sqlite3
from flask import Flask

DB_DIRECTORY = '/var/www/groja.com/htdocs/groja.com/db/'
NAME_EMAIL_TABLE = DB_DIRECTORY + 'NameEmail.db'

#
#  Note: we know, this file has no routes!
#  However, we import and declare app so we can use it to call open_resource
#  (and maybe more later)
#
app = Flask(__name__)

# =============================================================================
#
# Functions
# ---------


def drop_table():

    """ Drop the table exists (if it exists) """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        curs.execute('DROP TABLE IF EXISTS NameEmail')
    return True


#  Reference: https://www.sqlite.org/datatype3.html
#  Note: date_* columns are stored as integers:
#     "INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC"
#
def create_table():

    """ Create the table and the database (if necessary) """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        with app.open_resource(DB_DIRECTORY + 'NameEmailSchema.sql', mode='r') as nameEmailSchema:
            connection.executescript(nameEmailSchema.read())
            connection.commit()
    return True


def seed_table():

    """ Insert a row in the table, as a sanity check """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        curs.execute(
            "INSERT INTO NameEmail (name,email) VALUES (?,?)",
            ('Joe', 'joe@joe.com')
        )
    return True

# =============================================================================
#
# When run as a module, drop, create, and seed the table
#
if __name__ == '__main__':
    drop_table()
    create_table()
    seed_table()
