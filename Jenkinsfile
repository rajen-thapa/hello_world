pipeline {
    agent any
 stages {
  stage('Docker Build and Tag') {
           steps {
              
                sh 'docker build -t ibanez6123/python_app:latest .' 
                sh 'docker tag ibanez6123/python_app:latest ibanez6123/python_app:1.0'
                sh 'docker tag ibanez6123/python_app:latest ibanez6123/python_app:$BUILD_NUMBER'
               
          }
        }
     
  stage('Publish image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "Dockerhub_creds", url: "" ]) {
          sh  'docker push ibanez6123/python_app:1.0'
          sh  'docker push ibanez6123/python_app:$BUILD_NUMBER' 
        }
                  
          }
        }
     
      stage('Run Docker container on Jenkins Agent') {
             
            steps {
                sh "docker run -d -p 4030:4030 ibanez6123/python_app:1.0"
            }
        }
    }
}
