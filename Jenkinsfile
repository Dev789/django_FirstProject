pipeline{
    agent any
    stages{
        stage("Docker Image Build"){
            steps{
                docker build -tag django-pipeline .
            }
        }
    }
}