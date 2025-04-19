pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dsnkumar121/project"   
        IMAGE_TAG = "${BUILD_NUMBER}"          
        PORT = "5000"
        K8S_DEPLOY_DIR="."
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'cbbea2b1-6cb4-441c-a333-90dbe083d501', url: 'https://github.com/DSNdinesh/project.git'
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
               withCredentials([usernamePassword(credentialsId: '7064bfe2-1c4b-4a26-b340-6ca17c5ad1b9', passwordVariable: 'dockerpwd', usernameVariable: 'dockeruser')]){
                    sh '''
                    docker login -u $dockeruser -p $dockerpwd
                    docker push $DOCKER_IMAGE:$IMAGE_TAG
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅d ocker image pushed successfully!'
        }
        failure {
            echo '❌ Docker image push failed!'
        }
    }

    stage('depoly k8s') {
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
            echo '✅k8s deploy successfully!'
        }
        failure {
            echo '❌ k8s deploy failed!'
        }
    }


}
