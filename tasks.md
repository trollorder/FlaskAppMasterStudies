
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

## Tasks To Do
- Complete the Post Request to add a New Movie into the Database with Data Validation
- Implement a Manage Movies Tab with a Button to Delete Existing Movies from the Database
- There are 5000 movies in the database, display it 100 by 100 at one time, paginated.
- Ensure the table can be sorted by rating and filtered by name across the entire database.

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