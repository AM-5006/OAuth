pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Activate Virtual Environment') {
            steps {
                script {
                    // Ensure Bash shell is used
                    def shell = isUnix() ? 'sh' : 'bat'

                    // Activate the virtual environment
                    def activateScript = "/home/ubuntu/env/bin/activate"
                    sh "${shell} -c '. ${activateScript}'"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def projectDir = "/home/ubuntu/project"

                    // Go to the project directory
                    dir(projectDir) {
                        // Stop Gunicorn
                        sh 'sudo supervisorctl stop gunicorn'

                        // Pull latest changes from the repository (assuming 'master' branch)
                        sh 'git pull origin master'

                        // Start Gunicorn
                        sh 'sudo supervisorctl start gunicorn'

                        // Restart Nginx
                        sh 'sudo service nginx restart'
                    }
                }
            }
        }
    }
}
