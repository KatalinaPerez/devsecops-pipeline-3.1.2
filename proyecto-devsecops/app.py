from flask import Flask, request 
import re
import subprocess

app = Flask(__name__)
@app.route('/') 
def index(): 
    return "<h1>Servicio Web DevSecOps Activo - Katalina Perez</h1>" 
@app.route('/ping') 
def ping(): 
    ip = request.args.get('ip', '127.0.0.1') 
    
    # Validación estricta: Solo permite formato IPv4 (ej. 127.0.0.1)
    ip_pattern = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if not re.match(ip_pattern, ip):
        return "<pre>Error 400: Entrada invalida. No se permiten caracteres especiales o comandos inyectados.</pre>", 400
    #Ejecución segura mediante subprocesos sin invocar shell
    try:
        result = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True, timeout=5)
        output = result.stdout
    except Exception as e:
        output = f"Error al ejecutar el comando ping: {str(e)}"
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)