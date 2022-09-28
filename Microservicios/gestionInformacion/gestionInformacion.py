import logging, datetime
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from modelos import db, Usuario


import logging
from flask import Flask

app = Flask(__name__)


class VistaGestionInformacion(Resource):

    def getUsuario(usuario, contrasena):
        usuarioExistente = db.session.query(Usuario.id, Usuario.usuario).filter(Usuario.usuario == usuario, 
            Usuario.contrasena == contrasena).first()
        db.session.commit()
        if usuarioExistente is None:
            return None
        return usuarioExistente
    