from tg.configuration import AppConfig
from repoze.who.plugins.auth_tkt import AuthTktCookiePlugin
from repoze.who.plugins.basicauth import BasicAuthPlugin
import os

authtkt = AuthTktCookiePlugin('authtkt', 'authtkt')
basicauth = BasicAuthPlugin("something")

import pythondispatchms
from pythondispatchms import model, lib

base_config = AppConfig()
base_config.renderers = []


# True to prevent dispatcher from striping extensions
# For example /socket.io would be served by "socket_io"
# method instead of "socket".
base_config.disable_request_extensions = False

# Set None to disable escaping punctuation characters to "_"
# when dispatching methods.
# Set to a function to provide custom escaping.
base_config.dispatch_path_translator = True

base_config.prefer_toscawidgets2 = True

base_config.package = pythondispatchms

# Enable json in expose
base_config.renderers.append('json')

# Set the default renderer
base_config.renderers.append('mako')
base_config.renderers.append('kajiki')
base_config['templating.kajiki.strip_text'] = False  # Change this in setup.py too for i18n to work.

base_config.default_renderer = 'mako'

base_config.sa_auth.cookie_secret = "2a817308-b0ea-4ca7-bb42-00a20c941280"
# Configure Sessions, store data as JSON to avoid pickle security issues
base_config['session.enabled'] = True
base_config['session.data_serializer'] = 'json'
# Configure the base SQLALchemy Setup
base_config.use_sqlalchemy = True
base_config.model = pythondispatchms.model
base_config.DBSession = pythondispatchms.model.DBSession
# Configure the authentication backend
base_config.auth_backend = 'htpasswd'
# YOU MUST CHANGE THIS VALUE IN PRODUCTION TO SECURE YOUR APP

# what is the class you want to use to search for users in the database


from tg.configuration.auth import TGAuthMetadata


# This tells to TurboGears how to retrieve the data for your user
class ApplicationAuthMetadata(TGAuthMetadata):
    def __init__(self, sa_auth):
        self.sa_auth = sa_auth

    def get_user(self, identity, userid):
        # As we use htpasswd for authentication
        # we cannot lookup the user in a database,
        # so just return a fake user object
        from tg.util import Bunch
        return Bunch(display_name=userid, user_name=userid)

    def get_groups(self, identity, userid):
        # If the user is manager we give him the
        # managers group, otherwise no groups
        if userid == 'manager':
            return ['managers']
        else:
            return []

    def get_permissions(self, identity, userid):
        return []

base_config.sa_auth.authmetadata = ApplicationAuthMetadata(base_config.sa_auth)
from repoze.who.plugins.basicauth import BasicAuthPlugin
from repoze.who.plugins.htpasswd import HTPasswdPlugin, plain_check

app_dir = os.getenv('dispatch_DIR')
if app_dir is None:
    app_dir = os.getcwd()
password_file=app_dir+'/passwd_file'

base_config.sa_auth.authenticators = [('htpasswd', HTPasswdPlugin(password_file, plain_check))]

# In case ApplicationAuthMetadata didn't find the user discard the whole identity.
# This might happen if logged-in users are deleted.
base_config['identity.allow_missing_user'] = False

# You can use a different repoze.who Authenticator if you want to
# change the way users can login
# base_config.sa_auth.authenticators = [('myauth', SomeAuthenticator()]

# You can add more repoze.who metadata providers to fetch
# user metadata.
# Remember to set base_config.sa_auth.authmetadata to None
# to disable authmetadata and use only your own metadata providers
# base_config.sa_auth.mdproviders = [('myprovider', SomeMDProvider()]

# override this if you would like to provide a different who plugin for
# managing login and logout of your application


# You may optionally define a page where you want users to be redirected to
# on login:


# You may optionally define a page where you want users to be redirected to
# on logout:
base_auth = BasicAuthPlugin('MyTGApp')

base_config.sa_auth.identifiers = [('basicauth', base_auth)]

base_config.sa_auth.form_identifies = False
base_config.sa_auth.challengers = [('basicauth', base_auth)]
