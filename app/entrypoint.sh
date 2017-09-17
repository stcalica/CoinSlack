#!/bin/bash
gunicorn -b :5000 wsgi:app
