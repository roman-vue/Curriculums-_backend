# Importaciones
from flask import Flask
from flask_pymongo import PyMongo
from routes.index import index_bp 

# Inicializar flask
app = Flask(__name__)

# Registrar Blueprints de rutas
app.register_blueprint(index_bp)

# Conexion a mongo
app.config['MONGO_URI']='mongodb+srv://Curr_ADMIN:Kv4eGREjttoWv7qL@curriculumsdb.rd9hs.mongodb.net/Curriculums_ex?retryWrites=true&w=majority'

mongo = PyMongo(app)



