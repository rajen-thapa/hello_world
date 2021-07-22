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
     stage('docker stop container') {
         steps {
            sh 'docker ps -f name=mypythonapp -q | xargs --no-run-if-empty docker container stop'
            sh 'docker container ls -a -fname=mypythonapp -q | xargs -r docker container rm'
         }
       }
     
      stage('Run Docker container on Jenkins Agent') {
             
            steps {
                sh "docker run -d -p 4030:4030 --name=mypythonapp ibanez6123/python_app:1.0"
            }
        }
    }
}
