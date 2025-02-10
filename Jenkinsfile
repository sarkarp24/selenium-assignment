pipeline {
    agent any

    stages {
        stage('Python Env') {
            steps{
                sh '''
                    docker build -t selenium-assignment .
                    python --version
                    docker run selenium-assignment
                '''
            }
        }
    }
}
