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
                bat "docker-compose build"
            }
        }
        stage('Run'){
            steps {
                bat "docker-compose up -d"
            }
        }
        stage ('Test'){
            steps {
                bat "cd ./tests"
                bat "py e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                bat "docker compose down"
            }
        }
    }
}