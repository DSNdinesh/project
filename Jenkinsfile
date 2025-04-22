pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dsnkumar121/project1"
        IMAGE_TAG = "${BUILD_NUMBER}"
        PORT = "5000"
        K8S_DEPLOY_DIR = "."
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    credentialsId: 'cbbea2b1-6cb4-441c-a333-90dbe083d501',url: 'https://github.com/DSNdinesh/project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKER_IMAGE:$IMAGE_TAG .
                '''
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'f94735b2-2b3e-4abd-aeb5-450203b50cee', passwordVariable: 'dockerpwd', usernameVariable: 'dockeruser')]) {
                    sh '''
                    docker login -u $dockeruser -p $dockerpwd
                    docker push $DOCKER_IMAGE:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f ${K8S_DEPLOY_DIR}/k8s.yaml
                kubectl apply -f ${K8S_DEPLOY_DIR}/service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Docker image pushed and Kubernetes deployed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
