pipeline{
  agent any
  environment{
    APP_URL = 'http://127.0.0.1:5000'
  }
  stages{
    stage('Checkout'){
      steps{
        echo 'Fetching Project from Github'
        checkout scm
      }
    }
    stage('Install Dependencies'){
      steps{
        bat 'python -m pip install -r requirements.txt'
      }
    }
    stage('Start Flask Application'){
      steps{
        dir("${WORKSPACE}\\Automation\\simulator"){
          bat  'start "FlaskApp" /B python task1.py'
      }
      }
    }
    stage('Execute API Test'){
      steps{
        dir("${WORKSPACE}\\Robot_API_Project\\tests"){
          bat  'python -m robot test_2.robot'
      }
      }
    }
}
}
          
