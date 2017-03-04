##
#  Module to send an email notification of interest
#  Reference:
#     https://docs.python.org/3/library/email-examples.html
#
import smtplib
from email.mime.text import MIMEText

import os
GROJA_MAIL_FROM = os.environ.get( 'GROJA_MAIL_FROM' )
GROJA_MAIL_TO = os.environ.get( 'GROJA_MAIL_TO' )

##
#  Send an email getting the TO and FROM values from environment variables
#
#  Reference:
#     https://docs.python.org/3/library/email-examples.html
#
def send_interest_email( message_text ):
   ## print( 'In the send_test_email() in groja.py, message_text =', message_text )
   ## print( 'GROJA_MAIL_FROM:', GROJA_MAIL_FROM )
   ## print( 'GROJA_MAIL_TO:', GROJA_MAIL_TO )
   msg = MIMEText( message_text )
   msg['Subject'] = 'Indication of Interest on Groja.com'
   msg['From'] = GROJA_MAIL_FROM
   msg['To'] = GROJA_MAIL_TO
   server = smtplib.SMTP('localhost')
   server.send_message(msg)
   server.quit()
   print( 'Message sent!' )
   return True
