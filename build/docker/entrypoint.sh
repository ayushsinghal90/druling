#!/bin/bash

set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start supervisord
echo "Starting supervisord..."
exec supervisord -c /etc/supervisor/conf.d/supervisord.conf
