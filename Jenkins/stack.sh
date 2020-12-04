ssh jenkins@swarm-master << EOF
cd /home/a_cook8757/PracticalProject
docker stack deploy --compose-file docker-compose.yaml app
EOF
