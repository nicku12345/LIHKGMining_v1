"""
Defines the options for LIHKGThreadsManager
"""
from dataclasses import dataclass


@dataclass
class LIHKGThreadsManagerOptions:
    """
    Options for LIHKGThreadsManager.
    """

    # Used for fetching threads. Introduces a sleep between page fetches with
    # duration randomly chosen in the open interval (0, _sleep_time).
    # Its purpose is to create a more dynamic and less machinery behavior.
    # Default is 3 seconds
    SleepTime       : int = 3

    # Used for fetching threads. The fetch will retry on failure,
    # and stop once reaching this threshold
    # Default is 3 times
    MaxFailureCount : int = 3

    def ApplyOptions(self, LIHKGThreadsManagerCls):
        """
        Apply the options to the LIHKGThreadsManager class.

        :param LIHKGThreadsManagerCls: The class of LIHKGThreadsManager
        """
        LIHKGThreadsManagerCls._options = self
