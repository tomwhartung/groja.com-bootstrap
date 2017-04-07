""" groja.py: main application source for groja.com

Purpose: link routes to their corresponding templates
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  Chapter 3 of the "Flask Web Development" book (M. Grinberg, 2014)
"""

from groja_config import *
from flask import Flask, flash
from flask import redirect, render_template, request, session, url_for
from flask_bootstrap import Bootstrap
from form import NameEmailForm
from db_access import update_or_insert_name_email
from send_email import send_interest_email

app = Flask(__name__)

#
# Load the configuration settings and Bootstrap the app
#
app.config.from_object('groja_config.Config')
Bootstrap(app)

# =============================================================================
#
# Routes and view functions
# -------------------------

@app.route('/')
def home():
    """ Show the Home page """
    return render_template('home.html', homeSelected='selected')


@app.route('/about')
def about():
    """ Show the About page """
    return render_template('about.html', aboutSelected='selected')


@app.route('/booksandsites')
def booksandsites():
    """ Show the Books and Sites page """
    return render_template(
            'booksandsites.html',
            booksandsitesSelected='selected'
    )


@app.route('/yourportrait')
def yourportrait():
    """ Show the Your Portrait page """
    return render_template(
            'yourportrait.html',
            yourportraitSelected='selected'
    )


@app.route("/conversion/<interest>", methods=['GET', 'POST'])
def conversion(interest):

    """ Display and process conversion pages that contain a form """

    form = NameEmailForm(request.form)

    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        # print("In conversion, name: ", name, "email: ", email)

        if form.validate():
            session['name'] = name
            session['email'] = email
            if interest == 'groja':
                update_or_insert_name_email(name, email, portrait=1)
            elif interest == 'seeourminds':
                update_or_insert_name_email(name, email, newsletter=1)
            elif interest == 'tomwhartung':
                update_or_insert_name_email(name, email, consulting=1)
            else:
                update_or_insert_name_email(name, email)
            flash('Thanks, we will be in touch with you soon!')
            return redirect(url_for('thanks'))
        else:
            # print("form.errors:", form.errors)
            #
            # key = 'email', values = [] (list of error messages)
            #
            for key, value in form.errors.items():
                for message in value:
                    flash(message)
    else:
        form.name.data = ''
        form.email.data = ''

    if interest == 'groja':
        template_name = 'conversion_groja.html'
    elif interest == 'seeourminds':
        template_name = 'conversion_seeourminds.html'
    elif interest == 'tomwhartung':
        template_name = 'conversion_tomwhartung.html'
    else:
        template_name = 'home.html'

    return render_template(template_name, form=form)


@app.route("/thanks")
def thanks():

    """ Thank the visitor for sharing their email address """

    name = session.get('name')
    email = session.get('email')
    # print("In thanks, name: ", name, "email: ", email)
    send_interest_email(
            name + ' (' + email + ') ' +
            'has expressed an interest in buying a spiritual portrait!'
    )
    return render_template('thanks.html', name=name)

# =============================================================================
#
# Run the app!
#
if __name__ == '__main__':
    app.run()
