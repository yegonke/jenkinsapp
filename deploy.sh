#!/bin/sh

ssh -o StrictHostKeyChecking=no -i $MASTER_SSH_KEY "${MASTER_SSH_USER}@${MASTER_HOST}" << 'ENDSSH'
    cd ~/app 
    # && cat .env
    export $(cat .env | xargs)
    echo "Starting deployment..."
    echo "-------------------------------------------------------------------------------------------------"
    echo $CI_DEPLOY_PASSWORD | docker login -u $CI_DEPLOY_USER $CI_REGISTRY --password-stdin
    docker pull $DJANGO_IMAGE
    docker pull $NGINX_IMAGE
    docker-compose -f docker-compose.prod.yml up -d
ENDSSH
