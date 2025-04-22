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
                withCredentials([usernamePassword(credentialsId: 'a88f6e8e-b9ec-47e1-83e2-48a23b55f385', passwordVariable: 'dockerpwd', usernameVariable: 'dockeruser')]) {
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
                kubectl rollout restrt deployment my-app -n my-project
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
