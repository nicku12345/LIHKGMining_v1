from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def DatabaseInitApp(app, db=db):
    db.init_app(app)

    from mining.database.models.User import User
    from mining.database.models.Thread import Thread
    from mining.database.models.Message import Message

    with app.app_context():
        db.create_all()