pipeline{
		agent any
		stages{
			stage('Install Requirements'){
				steps{
					sh "bash Jenkins/requirements.sh"
				}
			}
			stage('Ansible') {
			    steps{
				ansiblePlaybook credentialsId:'private-key', installation:'ansible', inventory:'inventory', playbook:'playbook.yaml', disableHostKeyChecking: true
				}
			}
			stage('Testing'){
				steps{
					sh "bash Jenkins/testing.sh"
					
				}
			}
			stage('Build Images and Push'){
				steps{
					sh "bash Jenkins/docker.sh"
				}
			}
			stage('Deploy Stack'){
				steps{
					sh "bash Jenkins/stack.sh"
				}
			}
		}    
}
