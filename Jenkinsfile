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
        bat  'start "FlaskApp" /B python ../../../../../Python_training/Automation/simulator/task1.py'
      }
    }
    stage('Execute API Test'){
      steps{
        bat  'python -m robot ../../../../../Python_training/Robot_API_Project/tests/test_2.robot'
      }
    }
}
}
          
