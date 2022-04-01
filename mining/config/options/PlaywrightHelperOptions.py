"""
Defines the options for playwright helper
"""
from dataclasses import dataclass


@dataclass
class PlaywrightHelperOptions:
    """
    Options for PlaywrightHelper
    """

    # Used for defining the timeout limit for page.goto method
    # Default is 1 minute = 60,000 ms
    TimeoutMSLimit  : int = 60000

    def ApplyOptions(self, PlaywrightHelperCls):
        """
        Apply the options to the PlaywrightHelper class.

        :param PlaywrightHelperCls: The class of PlaywrightHelper
        """
        PlaywrightHelperCls._options = self
