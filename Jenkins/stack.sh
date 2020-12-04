ssh jenkins@swarm-master << EOF
docker pull michaelacook1/serv1i:latest
docker pull michaelacook1/serv2i:latest
docker pull michaelacook1/serv3i:latest
docker pull michaelacook1/serv4i:latest
cd PracticalProject/
docker stack deploy --compose-file docker-compose.yaml app
EOF
