from flaskblog import create_app, db
from flask.cli import with_appcontext

app = create_app()

with app.app_context():
    db.create_all()