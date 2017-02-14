##
# Flask configuration for groja.com
# ---------------------------------
# After a bit of research, we are going to use the method presented here:
#   http://flask.pocoo.org/docs/0.11/config/
# Another resource:
#   https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
#
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config( object ):
   DEBUG = False
   TEMPLATES_AUTO_RELOAD = True
   SEND_FILE_MAX_AGE_DEFAULT = 0
   CSRF_ENABLED = True
   SECRET_KEY = 'abcdefgHIJKLMNOPqRsTuVwXyZ'

class ProductionConfig( object ):
   DEBUG = False
   TESTING = False

class DevelopmentConfig( object ):
   DEBUG = True
   TESTING = False

class TestingConfig( object ):
   DEBUG = True
   TESTING = True
