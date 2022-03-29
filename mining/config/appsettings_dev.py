"""
The appsettings of dev env.
"""
from mining.config.base_appsettings import Appsettings
from mining.config.database_secrets.ConnectionStrings import DEV_CONNECTION_STRING

APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI=DEV_CONNECTION_STRING,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    IS_TEST=False,
    IS_AUTO_FETCH_LIHKGTHREADJOBS=False
)
