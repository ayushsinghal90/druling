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

## Useful commands

### Adding package in requirement txt
   ```commandline
   pip freeze > requirements.txt
   ```


## API Usage

### File Upload Endpoint

- **URL**: `/api/upload/`
- **Method**: `POST`
- **Form Data**:
  - `file`: The transcript file to upload (.txt)

## Example

```bash
curl -X POST -F "file=@path/to/transcript.txt" http://localhost:8000/api/upload/
