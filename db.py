from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# init the db and create tables


def db_init(app):
    db.init_app(app)

    # creates tables if db doesnt aleady exist
    with app.app_context():
        db.create(all)


g
