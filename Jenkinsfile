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
                    def activateScript = "/home/ubuntu/env/bin/activate"
                    // Use the source command to activate the virtual environment
                    sh ". ${activateScript}"
                }
            }
        }

        stage('Pull Code Changes') {
            steps {
                script {
                    def projectDir = "/home/ubuntu/project"

                    // Go to the project directory
                    dir(projectDir) {
                        // Pull latest changes from the repository (assuming 'master' branch)
                        sh 'git pull origin master'
                    }
                }
            }
        }
    }
}
