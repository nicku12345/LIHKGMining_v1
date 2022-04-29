"""
The appsettings for test env
"""
from mining.config.base_appsettings import Appsettings
from mining.config.options.LIHKGThreadsManagerOptions import LIHKGThreadsManagerOptions
from mining.config.options.PlaywrightHelperOptions import PlaywrightHelperOptions
from mining.config.options.LIHKGThreadsWorkerOptions import LIHKGThreadsWorkerOptions
from mining.config.options.BaseWorkerOptions import BaseWorkerOptions
from mining.config.options.LIHKGThreadsWorkQueueOptions import LIHKGThreadsWorkQueueOptions


APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI="sqlite:///data/sqlite/db_test.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=False,
    IS_TEST=True,
    LIHKGThreadsManagerOptions=LIHKGThreadsManagerOptions(SleepTime=3, MaxFailureCount=3),
    PlaywrightHelperOptions=PlaywrightHelperOptions(TimeoutMSLimit=60000),
    LIHKGThreadsWorkerOptions=LIHKGThreadsWorkerOptions(IsAutoFetchLIHKGThreadJobs=False),
    BaseWorkerOptions = BaseWorkerOptions(SleepTime=5),
    LIHKGThreadsWorkQueueOptions=LIHKGThreadsWorkQueueOptions(DiscardJobTimeLimit=259200)
)
