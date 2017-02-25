##
# groja.py: main application source for groja.com
# --------------------------------------------------
# Purpose: link routes to their corresponding templates
# Reference: Chapter 3 of the "Flask Web Development" book
#
from flask import Flask, flash
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
# Display contactme page with the form, and process it when it comes back
#
@app.route("/contactme", methods=['GET', 'POST'])
def contactme():
   form = NameEmailForm( request.form )

   if request.method == 'POST':
      name = form.name.data
      email = form.email.data
      print( "name: ", name, "email: ", email )

      if form.validate():
         session['name'] = name
         insert_name_email( name, email, portrait=1 )
         flash( 'Thanks, we will be in touch with you soon!' )
         return redirect( url_for('thanks') )
      else:
         ## print( "form.errors:", form.errors )
         #
         #  key = 'email', values = [] (list of error messages)
         #
         for key, value in form.errors.items():
            for message in value:
               flash( message )
   else:
      form.name.data = ''
      form.email.data = ''

   return render_template( 'contactme.html', form=form )

##
# Thank the visitor for sharing their email address
#
@app.route( "/thanks" )
def thanks():
   name = session.get( 'name' )
   return render_template( 'thanks.html', name=name )

##
# Run the app!
#
if __name__ == '__main__' :
   app.run()
