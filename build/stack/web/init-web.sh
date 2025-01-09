# Apply database migrations
python manage.py migrate

# Set up email templates with the --force option
python manage.py setup_email_templates

# Start the Django development server
python manage.py runserver 0.0.0.0:3000