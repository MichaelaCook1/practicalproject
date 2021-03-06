#!/bin/bash
ssh swarm-master << EOF
docker pull michaelacook1/service1:latest
docker pull michaelacook1/service2:latest
docker pull michaelacook1/service3:latest
docker pull michaelacook1/service4:latest
docker pull michaelacook1/db:latest
git clone https://github.com/MichaelaCook1/practicalproject.git
cd practicalproject/
docker-compose pull
docker stack deploy --compose-file docker-compose.yaml app
EOF
