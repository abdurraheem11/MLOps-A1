pipeline {
    agent {
        docker { 
            image 'docker:latest' 
            args '-v /var/run/docker.sock:/var/run/docker.sock' 
        }
    }
    environment {
        registryCredential = 'dockerhub-id'
        IMAGE_NAME = 'abdurraheemqureshi/mlops-a1'
        TAG = 'latest'
    }
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
                subject: 'Build Successful',
                body: 'The docker image was successfully pushed to Dockerhub! Well done!'
            )
        }
    }
}

