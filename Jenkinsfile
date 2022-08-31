pipeline{
    agent any
    stages{
        stage("Docker Image Build"){
            steps{
                // echo("This is docker")
                docker build -tag django-pipeline .
            }
        }
    }
}