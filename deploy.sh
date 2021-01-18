#!/bin/bash

echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
# docker login --username=joleesoftwire --password=$HEROKU_API_KEY registry.heroku.com
docker push joleesoftwire/todoapp:$TRAVIS_BRANCH
docker tag joleesoftwire/todoapp registry.heroku.com/jol-todoapp/web
docker push registry.heroku.com/jol-todoapp/web
heroku container:release --app jol-todoapp web