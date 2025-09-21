# Voice-to-Text & Translation API

A Django/DRF project for converting voice recordings to plain text and translated text, with user authentication (JWT).

Features:
- Convert audio files to text using AI models (e.g., Whisper)
- Translate the extracted text into multiple languages
- User registration and login with JWT authentication
- API documentation using Swagger / drf-spectacular

Installation & Setup:

1. Clone the project:
   ```bash
    git clone <repo-url>
   ```
   ```bash
   cd <project-folder>
   ```

3. Activate virtual environment:

    Linux / Mac:
   ```bash
    python -m venv venv
   ```
   ```bash
    source venv/bin/activate
   ```

    Windows:
   ```bash
    python -m venv venv
   ```
   ```bash
    venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```

Running the Project with Docker:

1. Build and Run:
   ```bash
    sudo docker-compose up --build -d
   ```

2. Create Database Tables:
   ```bash
    sudo docker exec -it backend bash
   ```
     ```bash
     python manage.py migrate
   ```
