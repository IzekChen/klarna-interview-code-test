#/bin/bash
FLASK_APP=./app/server.py FLASK_ENV=production FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=8080 flask run
