"""
Defines the options for LIHKG threads work queue
"""
from dataclasses import dataclass


@dataclass
class LIHKGThreadsWorkQueueOptions:
    """
    Options for LIHKGThreadsWorkQueue
    """

    # A limit for a job to be considered "old"
    # units in second
    DiscardJobTimeLimit : int = 3 * 60 * 60

    def ApplyOptions(self, LIHKGThreadsWorkQueueCls):
        """
        Apply the options to the LIHKGThreadsWorkQueue class.

        """
        LIHKGThreadsWorkQueueCls._options = self
