##
#  Create a sqlite3 table (db) named NameEmail
#  Create the db, create the table, seed in one row of data
#  Reference for Flask DB patterns:
#     http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
#
import sqlite3
## DB_DIRECTORY = '../db/'
DB_DIRECTORY = '/var/www/groja.com/htdocs/groja.com/db/'
NAME_EMAIL_TABLE = DB_DIRECTORY + 'NameEmail.db'

#
#  Note: we know, this file has no routes!
#  However, we import and declare app so we can use it to call open_resource
#  (and maybe more later)
#
from flask import Flask
app = Flask(__name__)

################################################################################
#  Functions
#  ---------
##
#  If the table exists, drop it
#  Makes it easy to start fresh (e.g., when changing the schema)
#
def drop_table():
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute( 'DROP TABLE IF EXISTS NameEmail' )
   return True

##
#  Create the table
#  If the database doesn't exist, this will create it as well
#  Reference: https://www.sqlite.org/datatype3.html
#  Note: date_* columns are stored as integers:
#     "INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC"
#
def create_table():
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      with app.open_resource( DB_DIRECTORY + 'NameEmailSchema.sql', mode='r' ) as nameEmailSchema:
         connection.executescript( nameEmailSchema.read() )
         connection.commit()
   return True

##
#  Seed the table
#  Insert a row (or two) in the table, as a sanity check
#
def seed_table():
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute(
         "INSERT INTO NameEmail (name,email) VALUES (?,?)",
            ( 'Joe', 'joe@joe.com' ) )
   return True

################################################################################
##
# Mainline code to drop, create, seed, and print the table
#
if __name__ == '__main__':
   drop_table()
   create_table()
   seed_table()
