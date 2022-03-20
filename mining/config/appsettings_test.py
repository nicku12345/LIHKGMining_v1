
from mining.config._appsettings_template import Appsettings

APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI="sqlite:///data/sqlite/db_test.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    IS_TEST=True
)