pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker-compose run --rm web python -m pytest'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker-compose push
                    '''
                }
            }
        }
        
        stage('Deploy to Dev Server') {
            steps {
                sshagent(credentials: ['dev-server-ssh']) {
                    sh '''
                        ssh user@dev-server 'cd /path/to/app && \
                        git pull && \
                        docker-compose pull && \
                        docker-compose up -d'
                    '''
                }
            }
        }
    }
}