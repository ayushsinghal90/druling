#!/bin/bash

set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Set up email templates with the --force option
python manage.py setup_email_templates

# Start supervisord
echo "Starting supervisord..."
exec supervisord -c /etc/supervisor/conf.d/supervisord.conf
