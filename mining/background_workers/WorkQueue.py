import queue
import threading
import time

class LIHKGThreadsWorkQueue:

    def __init__(self):
        self._queue = queue.Queue()

    def IsEmpty(self):
        return self._queue.empty()

    def Put(self, LIHKGThreadId: int, page: int = 1, isFullFetch: bool = False):
        self._queue.put((LIHKGThreadId, page, isFullFetch))

    def Get(self):
        return self._queue.get_nowait()


LIHKGThreadsWORKQUEUE = LIHKGThreadsWorkQueue()