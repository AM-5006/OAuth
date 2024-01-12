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
                    // Pull latest changes from the repository (assuming 'master' branch)
                    sh 'git pull origin master'
                }
            }
        }
    }
}
