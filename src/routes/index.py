import appConfig
from flask import Blueprint, jsonify,request,Response
from bson import json_util

# Creacion blueprint
index_bp = Blueprint('index',__name__)

# Ruta inicial
@index_bp.route('/',methods=['GET'])
def index():

    response = jsonify({
        'message': 'Bienvenido',
        'status': 200
    })
   
    return response

# Agregar datos usuario
@index_bp.route('/insertData',methods=['POST'])
def insertData():

    nombre = request.json['name']
    apellido = request.json['lastname']
    profesion = request.json['profession']
    telefono = request.json['phone']

    if nombre and apellido and profesion and telefono:

        appConfig.mongo.db.userData.insert_one(


            {
                'name': nombre,
                'lastname': apellido,
                'profession': profesion,
                'phone': telefono
            }

        )

        message = jsonify({

                'message': 'Usuario guardado',
                'name': nombre,
                'lastname': apellido,
                'profession': profesion,
                'phone': telefono

        })

        return message

    else :

        return error_400()
   
# Obtener usuarios
@index_bp.route('/getData',methods=['GET'])
def getData():

    data = appConfig.mongo.db.userData.find()
    response = json_util.dumps(data)

    return Response(response, mimetype='application/json')

#Error handlers
@index_bp.errorhandler(404)
def error_404(error=None):

    response = jsonify({
        'message': f'Recurso no encontrado {request.url}',
        'status': 404
    })

    response.status_code = 404

    return response

@index_bp.errorhandler(400)
def error_400(error=None):

    response = jsonify({
        'message': f'Bad Request',
        'status': 400
    })

    response.status_code = 400

    return response


