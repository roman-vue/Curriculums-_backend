from urllib import response
from flask import Blueprint, jsonify,request
import appConfig

# Creacion blueprint
index_bp = Blueprint('index',__name__)

# Ruta inicial
@index_bp.route('/',methods=['GET'])
def index():
    response = jsonify({
        'message':'Bienvenido',
        'status':200
    })
   
    return response

@index_bp.errorhandler(404)
def error_404(error=None):
    response = jsonify({
        'message':f'Recurso no encontrado{request.url}',
        'status':200
    })
    response.status_code = 404

    return response


