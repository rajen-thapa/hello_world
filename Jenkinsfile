pipeline {
    agent any
 stages {
  stage('Docker Build and Tag') {
           steps {
              
                sh 'sudo docker build -t ibanez6123/python_app:1.0 .' 
                sh 'sudo docker tag pythonapp ibanez6123/python_app:1.0'
                sh 'sudo docker tag pyhtonapp ibanez6123/python_app:$BUILD_NUMBER'
               
          }
        }
     
  stage('Publish image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "Dockerhub_creds", url: "https://hub.docker.com/repository/docker/ibanez6123/python_app" ]) {
          sh  'sudo docker push ibanez6123/python_app:1.0'
          sh  'sudo docker push ibanez6123/python_app:$BUILD_NUMBER' 
        }
                  
          }
        }
     
      stage('Run Docker container on Jenkins Agent') {
             
            steps {
                sh "sudo docker run -d -p 4030:80 ibanez6123/python_app:1.0"
            }
        }
    }
}
