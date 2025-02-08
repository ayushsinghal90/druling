import logging
import os
import signal
import threading
import time
import requests
import sys
from django.core.management.base import BaseCommand
from django.db import connections
from django.conf import settings

logger = logging.getLogger(__name__)


class SpotTerminationHandler:
    def __init__(self):
        self.terminating = threading.Event()
        self.spot_termination_url = "http://169.254.170.2/v2/spot/termination-notice"
        self.check_interval = 10  # Polling interval in seconds
        self.grace_period = 30  # Grace period in seconds

    def check_termination_notice(self):
        """Check if spot instance is scheduled for termination"""
        try:
            response = requests.get(self.spot_termination_url, timeout=2)
            return response.status_code == 200
        except requests.RequestException as e:
            logger.warning(f"Error checking termination notice: {e}")
            return False

    def graceful_shutdown(self, signum, frame):
        """Handle graceful shutdown of the Django application"""
        if self.terminating.is_set():
            return

        self.terminating.set()
        logger.info("Received termination notice, starting graceful shutdown...")

        try:
            # Close database connections
            for conn in connections.all():
                conn.close_if_unusable_or_obsolete()

            # Stop accepting new requests (if using Gunicorn)
            if hasattr(settings, "GUNICORN_PID_FILE") and os.path.exists(
                settings.GUNICORN_PID_FILE
            ):
                with open(settings.GUNICORN_PID_FILE) as f:
                    gunicorn_pid = int(f.read())
                    os.kill(gunicorn_pid, signal.SIGTERM)

            # Wait for ongoing requests to complete
            logger.info(
                f"Waiting {self.grace_period} seconds for ongoing requests to complete..."
            )
            time.sleep(self.grace_period)

            logger.info("Graceful shutdown completed")
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")
        finally:
            sys.exit(0)

    def start_monitoring(self):
        logger.info("Starting Fargate Spot termination monitoring...")

        # Register signal handlers
        signal.signal(signal.SIGTERM, self.graceful_shutdown)
        signal.signal(signal.SIGINT, self.graceful_shutdown)

        while not self.terminating.is_set():
            if self.check_termination_notice():
                self.graceful_shutdown(None, None)
            time.sleep(self.check_interval)


class Command(BaseCommand):
    help = "Starts the Fargate Spot termination handler"

    def handle(self, *args, **options):
        handler = SpotTerminationHandler()
        monitoring_thread = threading.Thread(target=handler.start_monitoring)
        monitoring_thread.daemon = True
        monitoring_thread.start()

        # Keep the main thread alive
        while not handler.terminating.is_set():
            time.sleep(1)
