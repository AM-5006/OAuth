pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Stop Services') {
            steps {
                script {
                    // Stop Supervisor
                    sh 'sudo supervisorctl stop all'
                }
            }
        }

        stage('Pull Code Changes') {
            steps {
                script {
                    // Pull latest changes from the repository (assuming 'master' branch)
                    sh 'git pull origin master'
                }
            }
        }

        stage('Start Services') {
            steps {
                script {
                    // Start Gunicorn
                    sh 'sudo supervisorctl reread'
                    sh 'sudo supervisorctl update'
                    sh 'sudo supervisorctl start all'

                    // Start Nginx
                    sh 'sudo service nginx restart'
                }
            }
        }
    }
}
