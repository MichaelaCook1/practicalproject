ssh jenkins@swarm-master << EOF
docker pull michaelacook1/serv1i:latest
docker pull michaelacook1/serv2i:latest
docker pull michaelacook1/serv3i:latest
docker pull michaelacook1/serv4i:latest
git clone https://github.com/MichaelaCook1/practicalproject.git
cd practicalproject/
docker stack deploy --compose-file docker-compose.yaml app
EOF
