##
# From Chapter 3 of the "Flask Web Development" book
# --------------------------------------------------
#
# Experimenting with templates
#
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask( __name__ )
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
# Run the app!
#
if __name__ == '__main__' :
   import socket
   hostname = socket.gethostname()

   if hostname == 'jane':
      debug_mode = True
   else:
      debug_mode = False

   print( 'debug_mode:', debug_mode )
   app.run( debug=debug_mode )
