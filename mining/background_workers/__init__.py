"""
Do necessary init for the background workers.
"""
from mining.background_workers.WorkQueue import LIHKGThreadsWORKQUEUE
from mining.background_workers.LIHKGThreadsWorker import lihkgThreadsWorker

def BackgroundWorkersInitApp(app):
    '''
    Do necessary init for the background workers.
    '''
    lihkgThreadsWorker.SetApp(app)
    lihkgThreadsWorker.Wakeup()
