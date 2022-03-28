"""
Create a Flask app
"""
from mining.app import LIHKGMiningApp

def create_app():
    """
    Create a Flask app
    """
    return LIHKGMiningApp.CreateApp()

if __name__ == "__main__":
    app = create_app()
