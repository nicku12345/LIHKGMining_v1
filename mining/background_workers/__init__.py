from mining.background_workers.WorkQueue import LIHKGThreadsWORKQUEUE
from mining.background_workers.LIHKGThreadsWorker import lihkgThreadsWorker

def BackgroundWorkersInitApp(app):
    lihkgThreadsWorker.SetApp(app)
    lihkgThreadsWorker.Wakeup()

