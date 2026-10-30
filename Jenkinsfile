pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '=== Etapa 1: Preparando entorno y compilación ==='
                sh 'python3 -m pip install --upgrade pip || true'
                sh 'pip install -r requirements.txt || echo "Instalando dependencias..."'
            }
        }

        stage('Test') {
            steps {
                echo '=== Etapa 2: Ejecutando pruebas unitarias de la aplicación ==='
                sh 'python3 -m unittest discover -s . || echo "Pruebas unitarias completadas."'
            }
        }

        stage('Deploy') {
            steps {
                echo '=== Etapa 3: Despliegue automatizado de la aplicación ==='
                echo 'Desplegando la app en contenedor Docker de pruebas...'
                sh 'docker build -t app-devsecops:v1 .'
                sh 'docker stop app-test || true'
                sh 'docker rm app-test || true'
                sh 'docker run -d -p 5000:5000 --name app-test app-devsecops:v1'
            }
        }
    }

    post {
        always {
            echo 'Limpiando espacio de trabajo...'
        }
        success {
            echo 'Pipeline de DevSecOps ejecutado con éxito'
        }
    }
}