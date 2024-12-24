# Druling

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


This will build all the services together
   ```commandline
   docker-compose build
   ```

This will build/re-build single service at a time
   ```commandline
   docker-compose --build web
   ```

### Running the containers

   ```commandline
    docker-compose up -d
   ```

### Stop the containers

   ```commandline
    docker-compose stop
   ```

### Stop and delete the containers along with their networks and temporary volumes.

   ```commandline
    docker-compose down
   ```

### Upload any file to localstack S3 bucket: Option 1

    * Copy and paste the desired file in s3_media_files folder and rename the file to sample.jpg
    * Re-build or restart your localstack docker container
    * The file will then automtically appear in the durling-menus-temp S3 bucket.

    NOTE: You can rename the file to something else but just make sure to copy paste the same name on line 25,
        in localstack_bootstrap/init-aws-resources.sh

### Upload any file to localstack S3 bucket: Option 2

    * Run below commands in your cmd or terminal

    docker cp </path/to/file/on/your/machine> <localstack-container-name>:/media/<file_name>
    docker exec <localstack-container-name> awslocal s3api put-object --bucket druling-menus-temp --key <file_name> --body /media/<file_name>

    For example: (On windows)

    docker cp C:\Users\singh\Downloads\pos2_sample.jpg druling-localstack-1:/media/pos2_sample.jpg
    docker exec druling-localstack-1 awslocal s3api put-object --bucket druling-menus-temp --key pos2_sample.jpg --body /media/pos2_sample.jpg
