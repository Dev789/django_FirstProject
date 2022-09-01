pipeline{
    agent{
        docker{
            stages{
                stage("Cloning Git"){
                    steps{
                        git(url: 'https://github.com/Dev789/django_FirstProject.git', branch: 'master', credentialsId: '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')
                    }
                }

                stage("building Image"){
                    steps{
                        script{
                            sh 'docker build -t test .'
                        }
                    }
                }
            }
        }   
    }
}

// pipeline {
//     agent none
//         stages {
//             stage('Maven Install') {
//                 agent {
//                     docker {
//                         image 'maven:3.5.0'
//                     }
//                 }
//                 steps {
//                     sh 'mvn clean install'
//                 }
//             }
//             stage('Docker Build') {
//                 agent any
//                 steps {
//                     sh 'docker build -t shanem/spring-petclinic:latest .'
//                 }
//             }
//         }
// }