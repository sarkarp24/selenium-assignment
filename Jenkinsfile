pipeline {
    agent any

    stages {
        stage('Python Env') {
            steps{
                sh '''
                    docker build -t selenium-assignment .
                    docker run selenium-assignment
                    python --version
                '''
            }
        }
    }
}
