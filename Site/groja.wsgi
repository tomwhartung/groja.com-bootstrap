##
# Trying to get groja.py to run on apache, via wsgi.
#
# References:
#   http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/
#   http://www.jakowicz.com/flask-apache-wsgi/
#
# http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#creating-a-wsgi-file :
#   "from yourapplication import app as application"
#
import sys
sys.path.insert(0, '/var/www/groja.com/htdocs/groja.com/Site')

from groja import app as application

