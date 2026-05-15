from flask import Flask, render_template, request


app = Flask(__name__)

PRECIO_TARRO = 9000


def calcular_compra_pintura(nombre, edad, cantidad):
    total_sin_descuento = cantidad * PRECIO_TARRO

    if edad >= 31:
        porcentaje_descuento = 25
    elif 18 <= edad <= 30:
        porcentaje_descuento = 15
    else:
        porcentaje_descuento = 0

    monto_descuento = total_sin_descuento * porcentaje_descuento / 100
    total_pagar = total_sin_descuento - monto_descuento

    return {
        "nombre": nombre,
        "edad": edad,
        "cantidad": cantidad,
        "precio_tarro": PRECIO_TARRO,
        "porcentaje_descuento": porcentaje_descuento,
        "total_sin_descuento": int(total_sin_descuento),
        "monto_descuento": int(monto_descuento),
        "total_pagar": int(total_pagar),
    }


def validar_usuario(usuario, contrasena):
    usuarios = {
        "juan": {"contrasena": "admin", "mensaje": "Bienvenido Administrador juan"},
        "pepe": {"contrasena": "user", "mensaje": "Bienvenido Usuario pepe"},
    }

    datos_usuario = usuarios.get(usuario.lower())
    if datos_usuario and datos_usuario["contrasena"] == contrasena:
        return datos_usuario["mensaje"], True

    return "Usuario o contraseña incorrectos", False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad = int(request.form.get("edad", 0))
        cantidad = int(request.form.get("cantidad", 0))
        resultado = calcular_compra_pintura(nombre, edad, cantidad)

    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    acceso_correcto = False
    usuario = ""

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "").strip()
        mensaje, acceso_correcto = validar_usuario(usuario, contrasena)

    return render_template(
        "ejercicio2.html",
        mensaje=mensaje,
        acceso_correcto=acceso_correcto,
        usuario=usuario,
    )


if __name__ == "__main__":
    app.run(debug=True)
