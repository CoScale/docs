#!/usr/bin/env bash

export JEKYLL_VERSION=3.5
docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  --volume="$PWD/vendor/bundle:/usr/local/bundle" \
  -e JEKYLL_UID=$(id -u) \
  -e JEKYLL_GID=$(id -g) \
  -it jekyll/jekyll:$JEKYLL_VERSION \
  bundle install

docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  --volume="$PWD/vendor/bundle:/usr/local/bundle" \
  -e JEKYLL_UID=$(id -u) \
  -e JEKYLL_GID=$(id -g) \
  -p 4000:4000 \
  -it jekyll/jekyll:$JEKYLL_VERSION \
  jekyll serve --watch --incremental
