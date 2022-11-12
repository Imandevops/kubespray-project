#!/bin/sh

gunicorn --config gunicorn_config.py authenticate.wsgi:application
