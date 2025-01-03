# Druling
Your one-stop solution for all you restaurant management.

## Project Setup

1. Clone the repository
2. Create .env file:
    ```bash
    cp .env.example .env
    ```
   NOTE: Please make sure that POSTGRES_DB is set as 'localhost' when running django app locally.
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
### Creating migrations

   ```commandline
    python manage.py makemigrations
   ```


## Run within Docker containers

### Build docker images
NOTE: Just make sure your requirements.txt and .env file is up-to-date.


* This will build all the services together
   ```commandline
   docker compose build
   ```

* This will build/re-build single service at a time
   ```commandline
   docker compose --build web
   ```

* Running the containers

   ```commandline
    docker compose up -d
   ```

* Stop the containers

   ```commandline
    docker compose stop
   ```

* Stop and delete the containers along with their networks and temporary volumes.

   ```commandline
    docker compose down
   ```

## Using S3 on localstack
We use localstack for AWS S3 while testing it is part of docker compose file.

* GUI here https://docs.localstack.cloud/user-guide/tools/localstack-desktop/
