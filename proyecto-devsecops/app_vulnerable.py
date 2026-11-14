from flask import Flask, request 
import os

app = Flask(__name__)
@app.route('/') 
def index(): 
    return "<h1>Servicio Web DevSecOps Activo - Katalina Perez</h1>" 
@app.route('/ping') 
def ping(): 
    # VULNERABILIDAD: Inyección de Comandos (Command Injection) 
    # Pasa el parámetro 'ip' directamente al shell del sistema sin sanitizar 
    ip = request.args.get('ip', '127.0.0.1') 
    output = os.popen(f"ping -c 1 {ip}").read() 
    return f"<pre>{output}</pre>" 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)