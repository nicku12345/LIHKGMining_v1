"""
Base class of a worker.
"""
import logging
import threading

class BaseWorker:
    """
    Base class of a worker.
    """

    def __init__(self, queue):
        self._logger = logging.getLogger("flask.app")
        self._queue = queue
        self._app = None

        # The time interval between each job polling
        self._sleep_time = 5

    def SetApp(self, app):
        '''
        Set up the app instance of the Worker.

        The app must be set up in order to access the current app context.

        :param app: a Flask instance, which is the main flask application
        '''
        self._app = app

    def Work(self):
        '''
        Base work method of the worker. It needs to be overridden in concrete worker classes.
        '''
        raise NotImplementedError()

    def Wakeup(self):
        '''
        Kicks start the Work method of the worker, provided that app has been
        set up and a real work method.
        '''
        if self._app is None:
            self._logger.error("Cannot wake up worker because app is not set. "
                               "Please set up the app in the BackgroundWorkersInitApp function")
            return

        self._logger.debug("Waking up worker...")
        t = threading.Thread(target=self.Work, daemon=True)
        t.start()
