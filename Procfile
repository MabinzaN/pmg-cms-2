web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn --workers 1 --worker-class gevent --timeout 30 --max-requests 3000 --max-requests-jitter 100 --log-file - --access-logfile - pmg:app
