from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Servicio Web DevSecOps Activo - Katalina " \
        "Perez</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request 
app = Flask(__name__)

@app.route('/') 
def index(): return "<h1>Servicio Web DevSecOps Activo - Katalina Perez</h1>" 
@app.route('/hello') 
def hello(): 
    # VULNERABILIDAD XSS REFLEJADO: 
    # Inserta la variable 'name' directamente en el HTML sin filtrar ni sanitizar 
    name = request.args.get('name', 'Invitado') 
    return f"<h1>Hola, {name}!</h1>" 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)