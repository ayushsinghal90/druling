# Financial Assistant

## Project Setup

1. Clone the repository
2. Create .env file:
    ```bash
    cp .env.example .env
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```
6. Run test cases
    ```bash
    python manage.py test
    ```

## Before commit

1. Run this command 
   ```bash
   pre-commit install
   ```
2. Enable Auto-Save:
   * Go to Preferences > Appearance & Behavior > System Settings.
   * Enable "Save files automatically if application is idle". 

This will save files automatically when you're not typing, triggering the File Watchers if configured.

## Useful commands

### Adding package in requirement txt
   ```commandline
   pip freeze > requirements.txt
   ```
