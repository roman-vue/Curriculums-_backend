# Importaciones
from flask import Flask
from flask_pymongo import PyMongo
from routes.index import index_bp 
from flask_swagger_ui import get_swaggerui_blueprint

# Inicializar flask
app = Flask(__name__)
BASE_PATH=app.root_path

#Swagger config
SWAGGER_URL = '/Docs'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint (
    SWAGGER_URL,API_URL,config={
        'app_name':'Curriculums_ex'
    }
)


# Registrar Blueprints de rutas
app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix = SWAGGER_URL)
app.register_blueprint(index_bp)

# Conexion a mongo
app.config['MONGO_URI']='mongodb+srv://Curr_ADMIN:Kv4eGREjttoWv7qL@curriculumsdb.rd9hs.mongodb.net/Curriculums_ex?retryWrites=true&w=majority'

#Inicializacion conexion a mongo
mongo = PyMongo(app)



