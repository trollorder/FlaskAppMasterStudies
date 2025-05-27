from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
# db = 'sqlite:///movies.db'

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # imports for routes
    from routes import register_routes
    register_routes(app, db)


    migrate = Migrate(app, db)
    return app
