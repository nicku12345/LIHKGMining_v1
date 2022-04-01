"""
Do necessary init for the managers.
"""
def ManagersInitApp(app, appsettings):
    """
    Do necessary init for the managers.
    """
    from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager
    from mining.managers.helpers.PlaywrightHelper import PlaywrightHelper

    appsettings.LIHKGThreadsManagerOptions.ApplyOptions(LIHKGThreadsManager)
    appsettings.PlaywrightHelperOptions.ApplyOptions(PlaywrightHelper)
