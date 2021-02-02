#!/bin/bash

echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
docker push joleesoftwire/todoapp:$TRAVIS_BRANCH
docker tag joleesoftwire/todoapp registry.heroku.com/$HEROKU_APP_NAME/web
docker push registry.heroku.com/$HEROKU_APP_NAME/web
heroku container:release --app $HEROKU_APP_NAME web