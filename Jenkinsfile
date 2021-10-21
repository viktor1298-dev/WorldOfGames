pipeline {
    agent any
    stages {
        stage('GIT Pull') {
            steps {
                git branch: 'main', url: 'https://github.com/viktor1298-dev/WorldOfGames'
            }
        }
        stage('Build'){
            steps {
                sh "docker compose build"
            }
        }
        stage('Run'){
            steps {
                sh "docker compose up -d"
            }
        }
        stage ('Test'){
            steps {
                sh "cd ./tests"
                sh "py e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                sh "docker compose down"
            }
        }
    }
}