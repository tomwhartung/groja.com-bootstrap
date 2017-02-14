##
# From Chapter 3 of the "Flask Web Development" book
# --------------------------------------------------
#
# Experimenting with templates
#
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask( __name__ )

##
# Load the configuration settings
#
from config import *
app.config.from_object('config.Config')

print( 'TEMPLATES_AUTO_RELOAD 1: ', app.config['TEMPLATES_AUTO_RELOAD'] )
import socket
hostname = socket.gethostname()

if hostname == 'jane':
   app.config.from_object('config.DevelopmentConfig')
else:
   app.config.from_object('config.ProductionConfig')

print( 'TEMPLATES_AUTO_RELOAD 2: ', app.config['TEMPLATES_AUTO_RELOAD'] )

## app.config.from_envvar('YOURAPPLICATION_SETTINGS')

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
   print( 'debug_mode:', debug_mode )
   app.run( debug=debug_mode )
