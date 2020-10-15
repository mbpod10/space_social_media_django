

# Below are templates for Django and Flask.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload /yourdomain.com/' button on the 'Web' tab to make your site
# live.

# +++++++++++ VIRTUALENV +++++++++++
# If you want to use a virtualenv, set its path on the web app setup tab.
# Then come back here and import your application object as per the
# instructions below


# +++++++++++ CUSTOM WSGI +++++++++++
# If you have a WSGI file that you want to serve using PythonAnywhere, perhaps
# in your home directory under version control, then use something like this:
#
#import sys
#
# path = '/home/mbpod10/path/to/my/app
# if path not in sys.path:
#    sys.path.append(path)
#
#from my_wsgi_file import application  # noqa


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
from django.core.wsgi import get_wsgi_application
import django
import os
import sys
#
# assuming your django settings file is at '/home/mbpod10/mysite/mysite/settings.py'
# and your manage.py is is at '/home/mbpod10/mysite/manage.py'
path = '/home/mbpod10/space_social_media_django'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simplesocial.settings")

django.setup()
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
# then:
application = get_wsgi_application()


# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
#
#import sys
#
# The "/home/mbpod10" below specifies your home
# directory -- the rest should be the directory you uploaded your Flask
# code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
# ...or uploaded files to the directory "myproject", then you should
# specify "/home/mbpod10/myproject"
#path = '/home/mbpod10/path/to/flask_app_directory'
# if path not in sys.path:
#    sys.path.append(path)
#
#from main_flask_app_file import app as application  # noqa
#
# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.
