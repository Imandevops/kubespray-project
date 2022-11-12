from flask import Flask
from authenticate.config import Config



def create_app():
    app = Flask(__name__)


    app.config.from_object(Config)

    from authenticate.model.models import db,mg
    db.init_app(app)
    mg.init_app(app, db)
    

    from authenticate.resource.views import bp
    app.register_blueprint(bp)

    return app