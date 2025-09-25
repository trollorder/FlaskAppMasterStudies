# Flask App

This is a basic Flask application for IMDB Movies for user studies in a full stack manipulation task

## Requirements

- Python 3.11 ++
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/trollorder/FlaskAppMasterStudies.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Run the Flask development server:
    ```bash
    py run.py
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```


## Feature
IMDB Main Features
Movie
- Top 10 By Genre
- Best Movie all Time

Director
-Top By Genre
- Top All Time

Admin
- Add New Movie
- Manage Movies - Update + Delete

## Warm-Up Task to do
Ensure that the /movies route shows a new random movie. Ensure that the "Get New Movie" Button actually gets a new movie to be displayed.

## Tests 
```bash
py test_script.py
```


## DB Commands
``` bash
flask --app main db init
flask --app main db migrate
flask --app main db upgrade
```