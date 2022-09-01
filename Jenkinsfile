pipeline{
    agent any
    stages{
        stage("Cloning Git"){
            steps{
                git(url: 'https://github.com/Dev789/django_FirstProject.git', branch: 'master', credentialsId: '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')
            }
        }

        stage("building Image"){
            steps{
                sh 'docker build --tag django .'
            }
        }
    }
}