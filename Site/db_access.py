##
#  Routines to support accessing the sqlite3 table (db) named NameEmail
#  By default (when run on the command line) this program prints all rows
#  Reference for Flask DB patterns:
#     http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
#
import sqlite3
import datetime

DB_DIRECTORY = '../db/'
NAME_EMAIL_TABLE = DB_DIRECTORY + 'NameEmail.db'

################################################################################
#
#  Functions:
#  ----------
#
##
#  Insert a row into the table
#
def insert_name_email( name, email, consulting=0, newsletter=0, portrait=0 ):
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      ## cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)", (email,username,phone,password))
      curs.execute(
         "INSERT INTO NameEmail (name,email,consulting,newsletter,portrait) VALUES (?,?,?,?,?)",
            ( name, email, consulting, newsletter, portrait ) )
   return True

##
#  Insert a row of hard-coded values into the table
#  We wrote this before the above (general) function and are keeping it (for now)
#     because it might come in handy for debugging the general function someday.
#  Absolutely this is cruft and can be deleted, if desired!
#
def insert_hard_coded_name_email():
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute(
         "INSERT INTO NameEmail (name,email,date_added,date_changed) VALUES (?,?,?,?)",
            ( 'Sam', 'sam@sam.com', my_current_timestamp(), my_current_timestamp() ) )
   return True

##
#  Return a string containing the date and the time formatted the same as the
#  Sqlite3 CURRENT_TIMESTAMP used in the schema, i.e.,
#     CURRENT_TIMESTAMP returns dates in the format "1970-01-01 00:00:00"
#
def my_current_timestamp():
   my_time = datetime.time(1, 2, 3)
   my_date = datetime.date.today()
   my_current_timestamp = datetime.datetime.combine( my_date, my_time )
   return my_current_timestamp

##
#  Print all rows in the table to stdout
#
def print_table( line_prefix="" ):
   rows = get_data()
   see_data( rows, line_prefix )
   return True

##
#  Get the data
#
def get_data():
   rows = []
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute( 'SELECT * from NameEmail')
      rows = curs.fetchall()
   return rows

##
#  Print the data
#
def see_data( rows, line_prefix="" ):
   for row in rows:
      print( line_prefix, "row:", row )
   return True

##
#  Test our insert* Functions
#  Usage:
#     $ . ./env.sh
#     $ python
#     >>> from db_access import test_insert_functions
#     >>> test_insert_functions()
#  Or, use these commands to test on the command line:
#     $ . ./env.sh
#     $ python
#     from db_access import insert_hard_coded_name_email
#     >>> insert_hard_coded_name_email()
#     >>> from db_access import insert_name_email
#     >>> insert_name_email( 'june', 'june@may.com' )
#     >>> insert_name_email( 'april', 'april@may.com', portrait=1 )
#     >>> insert_name_email( 'pete', 'pete@example.com', consulting=1 )
#     >>> insert_name_email( 'mia', 'mia@example.com', newsletter=1 )
#
def test_insert_functions():
   print_table( "1:" )
   insert_hard_coded_name_email()
   print( '' )
   print_table( "2:" )
   insert_name_email( 'june', 'june@may.com' )
   print( '' )
   print_table( "3:" )
   insert_name_email( 'april', 'april@may.com', portrait=1 )
   print( '' )
   print_table( "4:" )
   insert_name_email( 'pete', 'pete@example.com', consulting=1 )
   print( '' )
   print_table( "5:" )
   insert_name_email( 'mia', 'mia@example.com', newsletter=1 )
   print( '' )
   print_table( "6:" )

##
# Mainline code to print the table
#
if __name__ == '__main__':
   print_table()
