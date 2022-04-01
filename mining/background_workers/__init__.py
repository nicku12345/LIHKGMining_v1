"""
Do necessary init for the background workers.
"""
from mining.background_workers.LIHKGThreadsWorkQueue import LIHKGThreadsWORKQUEUE
from mining.background_workers.LIHKGThreadsWorker import lihkgThreadsWorker, LIHKGThreadsWorker
from mining.background_workers.BaseWorker import BaseWorker

def BackgroundWorkersInitApp(app, appsettings = None):
    '''
    Do necessary init for the background workers.
    '''
    appsettings.BaseWorkerOptions.ApplyOptions(BaseWorker)
    appsettings.LIHKGThreadsWorkerOptions.ApplyOptions(LIHKGThreadsWorker)

    lihkgThreadsWorker.SetApp(app)
    lihkgThreadsWorker.Wakeup()
