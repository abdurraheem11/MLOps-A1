pipeline {
    agent any
    environment {
        registryCredential = 'dockerhub-id'
        IMAGE_NAME = 'abdurraheemqureshi/mlops-a1'
        TAG = 'latest'
        DOCKER_PATH = '/usr/local/bin'
    }
    stages {
        stage('Cloning Git Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/abdurraheem11/mlops-a1.git'
            }
        }
        stage('Check Docker Version') {
            steps {
                sh 'export PATH=$DOCKER_PATH:$PATH && docker --version'
            }
        }
        stage('Building our image') {
            steps {
                script {
                    sh 'export PATH=$DOCKER_PATH:$PATH && docker build -t ${IMAGE_NAME}:${TAG} .'
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        sh 'export PATH=$DOCKER_PATH:$PATH && docker push ${IMAGE_NAME}:${TAG}'
                    }
                }
            }
        }
    }
    post {
        success {
            emailext(
                to: 'i200917@nu.edu.pk',
                subject: 'Build Successful',
                body: 'The docker image was successfully pushed to Dockerhub! Well done!'
            )
        }
    }
}
