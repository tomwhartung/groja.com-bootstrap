##
# groja.py: main application source for groja.com
# --------------------------------------------------
# Purpose: link routes to their corresponding templates
# Reference: Chapter 3 of the "Flask Web Development" book
#
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask import redirect, render_template, request, session, url_for
from form import NameEmailForm
from db_access import insert_name_email

app = Flask( __name__ )

##
# Load the configuration settings
#
print( 'TEMPLATES_AUTO_RELOAD 0: ', app.config['TEMPLATES_AUTO_RELOAD'] )
from config import *
app.config.from_object('config.Config')
print( 'TEMPLATES_AUTO_RELOAD 1: ', app.config['TEMPLATES_AUTO_RELOAD'] )

##
#  Bootstrap the app
#
Bootstrap( app )

##
# Show the Home page:
#
@app.route( '/' )
def home() :
   return render_template( 'home.html', homeSelected='selected' )

##
# Show the About page:
#
@app.route( '/about' )
def about() :
   return render_template( 'about.html', aboutSelected='selected' )

##
# Show the Books and Sites page:
#
@app.route( '/booksandsites' )
def booksandsites() :
   return render_template( 'booksandsites.html', booksandsitesSelected='selected' )

##
# Show the Your Portrait page:
#
@app.route( '/yourportrait' )
def yourportrait() :
   return render_template( 'yourportrait.html', yourportraitSelected='selected' )

##
# Show the Books and Sites page:
#
@app.route( '/contactme' )
def contactme() :
   return render_template( 'contactme.html', contactmeSelected='selected' )

##
# Run the app!
#
if __name__ == '__main__' :
   app.run()
