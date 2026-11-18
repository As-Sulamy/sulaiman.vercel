#!/bin/sh
set -eu

mkdir -p staticfiles_build/static staticfiles_build/media
cp -R staticfiles/. staticfiles_build/static/
cp -R media/. staticfiles_build/media/
