pipeline {
    environment {
        registryCredential = 'dockerhub-id'
        IMAGE_NAME = 'abdurraheemqureshi/mlops-a1'
        TAG = 'latest' 
    }
    agent any
    stages {
        stage('Cloning Git Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/abdurraheem11/mlops-a1.git'
            }
        }
        stage('Building our image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }
    }
    post {
        success {
            emailext(
                to: 'i200917@nu.edu.pk',
                subject: 'Build Successful ',
                body: 'The docker image successfully pushed to Dockerhub! Well Done!'
            )
        }
    }
}