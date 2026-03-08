pipeline {
    agent any

    stages {

    stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/jatin1410/aceest-gym-devops.git'
    }
}

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-gym-app .'
            }
        }
    }
}