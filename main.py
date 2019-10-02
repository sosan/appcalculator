# -*- encoding: utf-8 -*-
"""
APP CALCULATOR 1.0
Programa donde creamos una calculadora para funcionar en
un movil desde web


"""

# importaciones
import os
from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap

from moduloTemplates import formsTemplates

# instancias e iniciaciones
app = Flask(__name__)
app.config["SECRET_KEY"] = "SEECRETO"
bootstrap = Bootstrap(app)

# iniciaciones variables globales . mejor usar global
resultado = False
operacion = None
numeroA = None
numeroB = None


# ruta entrada en el navegador
@app.route("/")
def home():
    templateBotones = formsTemplates.TemplateFormularioCalculadora()

    return render_template("index.html", template=templateBotones)

# @app.route("/<int:numero>", methods=["POST"])
# def recibirDatos(numero=-1):
#     pass

@app.route("/<operador>", methods=["POST"])
def recibirOperador(operador=""):

    global  operacion
    if request.form["operador"] == "x":
        operacion = "x"

    elif request.form["operador"] == "+":
        operacion = "x"

    elif request.form["operador"] == "-":
        operacion = "x"

    elif request.form["operador"] == "/":
        operacion = "x"

    elif request.form["operador"] == "=":
        operacion = "="

    return render_template("index.html", dato=request.form["operador"])
    #
    # global resultado
    # global numeroA
    # global numeroB
    #
    # if resultado == False:
    #     if numeroA is None:
    #         numeroA = numero
    #     if numeroB is None:
    #         numeroB = numero
    #         resultado = True
    #
    # else:
    #     if (operacion == "mas"):
    #         pass
    #     elif operacion == "menos":
    #         pass
    #     elif operacion == "mul":
    #         pass
    #     elif operacion =="div":
    #         pass
    #
    #     total = numeroA + numeroB
    #
    # if request.form["opcion"] == "1":
    #     print("opcion")


# @app.route("/<operador>", methods=["POST"])
# def recibiroperacion(operador=""):
#
#
#     global operacion
#     operacion = operador
#     return operacion



def calcularOperacion(numeroA, numeroB):
    pass


if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
