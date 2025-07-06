from flask_cors import CORS
from flask_restful import Api
from src.routes import register_routes
from extensions import app, db, ma
from config import Config
from flask_migrate import Migrate

app.config.from_object(Config)
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)
register_routes(api)

