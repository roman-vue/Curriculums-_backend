from flask import Blueprint,request
import appConfig

# Creacion blueprint
index_bp = Blueprint('index',__name__)

# Ruta inicial
@index_bp.route('/',methods=['POST'])
def index():
    
    return {'mensaje': 'Recibido'}