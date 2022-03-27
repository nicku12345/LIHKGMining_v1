"""
Create a Flask app
"""
from mining.app import LIHKGMiningApp

def create_app():
    """
    Create a Flask app
    """
    return LIHKGMiningApp.CreateApp()

app = create_app()
