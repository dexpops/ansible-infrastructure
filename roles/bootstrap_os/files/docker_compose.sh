#!/bin/bash
set -e

DOCKER_COMPOSE_INSTALL_PATH="/opt/bin"

if ! which ${DOCKER_COMPOSE_INSTALL_PATH}/docker-compose > /dev/null 2>&1; then
  echo "Download and install Docker compose."
  curl -sL "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" > ${DOCKER_COMPOSE_INSTALL_PATH}/docker-compose
  chmod +x ${DOCKER_COMPOSE_INSTALL_PATH}/docker-compose
fi

exit 0