
from mining.config.base_appsettings import Appsettings

APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI="sqlite:///data/sqlite/db_test.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    IS_TEST=True
)