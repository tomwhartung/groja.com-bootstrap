##
#  Routines to support accessing the sqlite3 table (db) named NameEmail
#  By default (when run on the command line) this program prints all rows
#  Reference for Flask DB patterns:
#     http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
#
import sqlite3
import datetime
from db_create import NAME_EMAIL_TABLE

################################################################################
#
#  Function definitions:
#  =====================
#  Database access functions are most important and so appear first
#  ----------------------------------------------------------------
##
#  Update an old or insert a new row into the table, as appropriate
#
def update_or_insert_name_email( name, email, id=0, consulting=-1, newsletter=-1, portrait=-1 ):
   ## print( 'In update_or_insert_name_email and NAME_EMAIL_TABLE =', NAME_EMAIL_TABLE )
   if id == 0:
      result = email_already_in_db( email )
      if result:
         id = result[0]
         print( 'Updating the email that is already in the db, id =', id )
         with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
            query = 'UPDATE NameEmail SET name = "' + name + '"'
            if consulting != -1:
               query += ', consulting = ' + str(consulting)
            if newsletter != -1:
               query += ', newsletter = ' + str(newsletter)
            if portrait != -1:
               query += ', portrait = ' + str(portrait)
            query += ' WHERE id = ' + str(id)
            curs = connection.cursor()
            curs.execute( query )
      else:
         # default ("-1") means not specified means "0" when inserting
         if consulting == -1:
            consulting = 0
         if newsletter == -1:
            newsletter = 0
         if portrait == -1:
            portrait = 0
         insert_name_email( name, email, consulting, newsletter, portrait )
   else:
      print( 'We got an id passed in, and we are not yet prepared to handle it:', id )

###   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
###      curs = connection.cursor()
###      curs.execute(
###         "INSERT INTO NameEmail (name,email,consulting,newsletter,portrait) VALUES (?,?,?,?,?)",
###            ( name, email, consulting, newsletter, portrait ) )

   return True

##
#  Check for existing email address
#  If it's there, return the row, else return False
#
def email_already_in_db( email ):
   result = False
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      ## query = 'SELECT * from NameEmail WHERE email = "' + email + "'"
      query = 'SELECT * from NameEmail WHERE email = "' + email + '"'
      curs.execute( query )
      row = curs.fetchone()
      print( 'in email_already_in_db, row:', row )
      result = row
   return result

##
#  Insert a row into the table
#
def insert_name_email( name, email, consulting=0, newsletter=0, portrait=0 ):
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute(
         "INSERT INTO NameEmail (name,email,consulting,newsletter,portrait) VALUES (?,?,?,?,?)",
            ( name, email, consulting, newsletter, portrait ) )
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


################################################################################
#
#  Functions for testing and development, etc.:
#  --------------------------------------------
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
#     $ python3
#     >>> from db_access import test_insert_functions
#     >>> test_insert_functions()
#  Or, use these commands to test on the command line:
#     $ . ./env.sh
#     $ python3
#     >>> from db_access import insert_hard_coded_name_email
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
