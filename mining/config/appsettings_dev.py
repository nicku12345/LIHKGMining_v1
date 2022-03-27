"""
The appsettings of dev env.
"""
from mining.config.base_appsettings import Appsettings

APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI="sqlite:///data/sqlite/db_dev.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    IS_TEST=False,
    IS_AUTO_FETCH_LIHKGTHREADJOBS=False
)
