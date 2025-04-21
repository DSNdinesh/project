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
                withCredentials([usernamePassword(credentialsId: 'd10f64e1-5d6f-488e-98b0-14ebc9ec6d7b', passwordVariable: 'dp', usernameVariable: 'du')]) {
                    sh '''
                    docker login -u $du -p $dp
                    docker push $DOCKER_IMAGE:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                sed "s/__BUILD_TAG__/$BUILD_TAG/g" k8s.yaml | kubectl apply -f -
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
