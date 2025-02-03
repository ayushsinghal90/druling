#!/bin/bash
set -e

# Function to gracefully shut down Gunicorn
shutdown() {
    echo "Shutdown signal received. Stopping Gunicorn gracefully..."

    # Gracefully stop Gunicorn workers (stops accepting new requests)
    kill -SIGTERM $GUNICORN_PID

    # Allow some time for in-progress requests to complete
    echo "Waiting for ongoing requests to finish..."
    sleep 10  # Adjust time as needed

    # Force kill Gunicorn if it's still running after the grace period
    kill -9 $GUNICORN_PID 2>/dev/null || true

    echo "Shutdown complete."
    exit 0
}

# Trap SIGTERM and SIGINT signals (container stop or AWS shutdown notice)
trap shutdown SIGTERM SIGINT

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Set up email templates with the --force option
echo "Setting up email templates..."
python manage.py setup_email_templates --force

# Start Gunicorn in the background with graceful timeout
echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 setup.wsgi:application --workers 4 --timeout 90 &

# Store the PID of the Gunicorn process
GUNICORN_PID=$!

# Poll AWS metadata service for spot termination notice
while true; do
    TERMINATION_INFO=$(curl -s http://169.254.169.254/latest/meta-data/spot/instance-action || true)
    if [ -n "$TERMINATION_INFO" ]; then
        echo "AWS Spot termination notice detected! Gracefully shutting down..."
        shutdown
    fi
    sleep 5
done

# Wait for Gunicorn to exit
wait $GUNICORN_PID
