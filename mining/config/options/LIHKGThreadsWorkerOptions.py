"""
Defines the options for LIHKGThreadsWorker
"""
from dataclasses import dataclass


@dataclass
class LIHKGThreadsWorkerOptions:
    """
    Options for LIHKGThreadsWorker
    """
    IsAutoFetchLIHKGThreadJobs  : bool = False

    def ApplyOptions(self, LIHKGThreadsWorkerCls):
        """
        Apply the options to the LIHKGThreadsWorker class

        :param LIHKGThreadsWorkerCls: The LIHKGThreadsWorker class
        """
        LIHKGThreadsWorkerCls._options = self
