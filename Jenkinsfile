pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
