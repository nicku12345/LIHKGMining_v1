from dataclasses import dataclass

@dataclass
class BaseWorkerOptions:
    """
    Options for base worker
    """
    SleepTime: int = 5

    def ApplyOptions(self, baseWorkerCls):
        """
        Apply the options to the base worker class

        :param baseWorkerCls: The base worker class
        """
        baseWorkerCls._baseOptions = BaseWorkerOptions
