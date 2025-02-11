# Whisper-Server

This repository demonstrates how to set up a basic Django project with the Django REST Framework (DRF) to create a simple API. The project exposes an endpoint that returns static data in JSON format. It does **not** require a database, making it lightweight and easy to set up.

## Features

- **Django**: The backend framework used to build the application.
- **Django REST Framework**: A powerful toolkit to create Web APIs.
- **Static Data**: The API serves static data (no database) for simplicity.

## Setup Instructions

Follow these steps to get the project up and running locally.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ayoosh007/Whisper-Server.git
cd Whisper-Server
```

### 2. Create and Activate a Virtual Environment using `venv`

It is recommended to use Python's built-in `venv` module to create a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Project Dependencies
ffmpeg is a dependency for whisper models:
### For Windows
```
choco install ffmpeg
```
or
go to the official ffmpeg site and install ffmpeg

Note: if Installing manually remember to add ffmpeg to your path as whisper calls it using subprocess module

### For Linux
Use your package manager to simply install ffmpeg

Install the necessary dependencies for the project:

```bash
pip install -r requirements.txt
```

### 4. Run the Development Server

Start the development server to begin using the API:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

### 5. Access the API

```
GET http://127.0.0.1:8000/transcribe/
```

This will return a list of items in JSON format.

## API Endpoints

- **GET `transcribe/`**: Gets you the transcription of the .wav file sent to the server
  
 ## Sample cURL Request
 ```
 curl -X POST http://127.0.0.1:8000/transcribe/ -F "file=@C:\path\to\your\file.wav"
 ```
## Project Structure

- **`myoopsprj/`**: The main Django project folder.
  - `settings.py`: Contains project-level settings.
  - `urls.py`: The routing configuration for the Django app.
- **`api/`**: The Django app handling the API functionality.
  - `views.py`: Contains views for processing requests and returning responses.
  - `serializers.py`: Contains the serializer to convert static data into JSON format.
  - `urls.py`: Contains URL routing for the API endpoints.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

