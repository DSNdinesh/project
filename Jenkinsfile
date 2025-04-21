pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dsnkumar121/project"
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
                withCredentials([usernamePassword(credentialsId: '4105d4a7-ce26-4862-86e3-4844cbb813b4', passwordVariable: 'dockerpwd', usernameVariable: 'dockeruser')]) {
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
                kubctl create namesapce name first
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
