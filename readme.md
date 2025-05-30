# Flask App

This is a basic Flask application for IMDB Movies

## Requirements

- Python 3.11
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

1. Set the `FLASK_APP` environment variable:
    ```bash
    export FLASK_APP=app.py
    ```

2. Run the Flask development server:
    ```bash
    py run.py
    ```

3. Open your browser and navigate to:
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

## Tasks To Do
- Complete the Post Request to add a New Movie into the Database with Data Validation
- Implement a Manage Movies Tab with a Button to Delete Existing Movies from the Database
- There are 5000 movies in the database, display it 100 by 100 at one time
- Ensure the Table can be sorted and filtered 


## DB Commands
``` bash
flask --app main db init
flask --app main db migrate
flask --app main db upgrade
```