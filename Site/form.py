##
#  Define the forms used by this app
#  For references, see the README.md file:
#     https://github.com/tomwhartung/always_learning_python/tree/master/13-flask_frankenforms_exp-4
#
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Optional, Required, Email

##
#  Define a form to get the visitor's name and email address
#
class NameEmailForm( FlaskForm ):
   name = StringField( 'Name:', validators=[Optional()] )
   email = StringField( 'Email:',
      [Required("Please share your email address so that we can contact you."),
       Email("Please enter a valid email address.")] )
   submit = SubmitField( 'Get Your Portrait' )

   def reset(self):
      blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
      self.process(blankData)
