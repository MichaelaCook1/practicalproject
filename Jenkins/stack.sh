ssh jenkins@swarm-master << EOF
cd /home/a_cook8757/PracticalProject
env SECRET_KEY=${SECRET_KEY} env DATABASE_URI=${DATABASE_URI} docker stack deploy --compose-file docker-compose.yaml app
EOF
