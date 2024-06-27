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
                sh 'docker-compose -f docker-compose-build.yml build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker-compose -f docker-compose-build.yml run --rm web python -m pytest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker-compose -f docker-compose-build.yml push
                    '''
                }
            }
        }
        
        // stage('Deploy to Dev Server') {
        //     steps {
        //         sshagent(credentials: ['dev-server-ssh']) {
        //             sh '''
        //                 ssh user@dev-server 'cd /path/to/app && \
        //                 git pull && \
        //                 docker-compose -f docker-compose-build.yml pull && \
        //                 docker-compose -f docker-compose-build.yml up -d'
        //             '''
        //         }
        //     }
        // }
    }
}