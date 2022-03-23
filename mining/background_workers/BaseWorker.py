import logging
import threading

class BaseWorker:

    def __init__(self, queue):
        self._logger = logging.getLogger("flask.app")
        self._queue = queue
        self._app = None
        self._sleep_time = 5

    def SetApp(self, app):
        self._app = app

    def Work(self):
        raise NotImplementedError()

    def Wakeup(self):
        if self._app == None:
            self._logger.error("Cannot wake up worker because app is not set. Please set up the app in the BackgroundWorkersInitApp function")
            return

        self._logger.info("Waking up worker...")
        t = threading.Thread(target=self.Work, daemon=True)
        t.start()