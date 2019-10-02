"""
MODULO COMO TEMPLATE PARA LOS FORMULARIOS

"""

from wtforms import Form, StringField, validators, SubmitField, ValidationError


class TemplateFormularioCalculadora(Form):
    botonnumero = SubmitField()
