"""
The appsettings of dev env.
"""
from mining.config.base_appsettings import Appsettings
from mining.config.database_secrets.ConnectionStrings import DEV_CONNECTION_STRING
from mining.config.options.LIHKGThreadsManagerOptions import LIHKGThreadsManagerOptions
from mining.config.options.PlaywrightHelperOptions import PlaywrightHelperOptions
from mining.config.options.LIHKGThreadsWorkerOptions import LIHKGThreadsWorkerOptions
from mining.config.options.BaseWorkerOptions import BaseWorkerOptions


APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI=DEV_CONNECTION_STRING,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=False,
    IS_TEST=False,
    LIHKGThreadsManagerOptions=LIHKGThreadsManagerOptions(SleepTime=3, MaxFailureCount=3),
    PlaywrightHelperOptions=PlaywrightHelperOptions(TimeoutMSLimit=60000),
    LIHKGThreadsWorkerOptions=LIHKGThreadsWorkerOptions(IsAutoFetchLIHKGThreadJobs=True),
    BaseWorkerOptions=BaseWorkerOptions(SleepTime=5)
)
