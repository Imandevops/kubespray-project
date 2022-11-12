from authenticate.authenticate import create_app
import warnings


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask_marshmallow import Marshmallow
application = create_app()