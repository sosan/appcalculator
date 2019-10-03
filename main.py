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
app.debug = True

# iniciaciones variables globales . mejor usar global. clase?
limpiar = False
siguienteNumero = False
operadorTexto = [""]
numeroA = -1
numeroB = -1
numeroATexto = []
numeroBTexto = []


# ruta entrada en el navegador
@app.route("/")
def home():
    templateBotones = formsTemplates.TemplateFormularioCalculadora()

    return render_template("index.html", template=templateBotones)


@app.route("/", methods=["POST"])
def recibirDatos():
    form = request.form

    global numeroA
    global numeroB

    for key in form.keys():
        if (key == "numero"):

            rellenarNumero(form[key])
            break

        elif (key == "operador"):

            if (len(numeroATexto) == 0):
                return render_template("index.html", dato="")

            mostrarfinal = rellenarOperador(form[key])

            if mostrarfinal == 2:

                try:

                    numeroA = float("".join(numeroATexto))
                    numeroB = float("".join(numeroBTexto))

                    resultado = calcularOperacion(
                        numeroA, numeroB, operadorTexto[0])

                    dat = "".join(
                        numeroATexto) + operadorTexto[0] + "".join(numeroBTexto) + "=" + str(resultado)
                    print(dat)
                    return render_template("index.html", dato=dat)

                except ValueError:
                    return "Error - REcargar pagina"
            elif mostrarfinal == 1:
                break
            elif mostrarfinal == 0:
                return render_template("index.html", dato=" ")

    dat = "".join(numeroATexto) + operadorTexto[0] + "".join(numeroBTexto)
    return render_template("index.html", dato=dat)


def calcularOperacion(numA, numB, operador):

        if operador == "+":
            return float(numA + numB)
        elif operador == "-":
            return float(numA - numB)
        elif operador == "x":
            return float(numA * numB)
        elif operador == "/":
            if (numeroB == 0):
                return "#Error#"
            else:
                return float(numA / numB)


def rellenarNumero(numero):
    global siguienteNumero
    global numeroATexto
    global numeroBTexto

    if siguienteNumero == False:
        numeroATexto.append(numero)
    else:
        numeroBTexto.append(numero)


def rellenarOperador(oper):
    global siguienteNumero
    global operadorTexto

    if oper == "+" or oper == "-" or oper == "x" or oper == "/":

        siguienteNumero = True
        operadorTexto[0] = oper
        return 1

    elif oper == "=":
        siguienteNumero = False
        # global limpiar
        # limpiar = True
        return 2

    elif oper == " ":
        limpiar()
        return 0


def limpiar():
    del numeroATexto[:]
    del numeroBTexto[:]
    operadorTexto[0] = ""
    numeroA = -1
    numeroB = -1


if __name__ == "__main__":
    app.run("127.0.0.1", 80, debug=True)
