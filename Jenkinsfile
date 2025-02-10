pipeline {
    agent any

    stages {
        stage('Python Env') {
            steps{
                sh '''
                    docker build -t selenium-assignment .
                    python --version
                '''
            }
            steps {
                withCredentials([string(credentialsId: 'FB_cred', variable: 'password')]) {
                    // some block
                    sh '''
                        echo "The password is: $password"  // For demonstration only - DO NOT echo passwords in real scripts!
                        python --version
                        python_script = """
                            import os
                            pwd = os.environ['password']
                            # Now use the password securely in your Python code
                            print(f"Password retrieved in Python: {pwd}") # For demonstration only - DO NOT print passwords in real scripts!
                        """
                        //sh "python -c \"${python_script}\""
                    '''
                }   
            }
        }
    }
}
