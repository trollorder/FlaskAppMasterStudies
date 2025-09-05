import requests
import json

# Test data for the add movies route
test_movie = {
    "id": 99999,
    "poster_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png",
    "title": "Fake_movie_1",
    "year": 2025,
    "certificate": "PG-13",
    "genre": "Action",
    "rating": 9.0,
    "metascore": 50,
    "director": "James",
    "cast": "James Bourne",
    "votes": 10000,
    "description": "This is a fake movie",
    "review_count": 2000,
    "review_title": "Fake movie testing Title",
    "review": "This is a placeholder for fake movies"
}

# API endpoint for adding movies
base_url = "http://localhost:5000"  
add_movie_endpoint = f"{base_url}/add-movie"

def test_add_movie():
    # Send POST request to add a movie
    response = requests.post(
        add_movie_endpoint,
        json=test_movie,
        headers={"Content-Type": "application/json"}
    )
    
    # Print response details
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    # Assert the response status code is 201 (Created) or 200 (OK)
    assert response.status_code in [200, 201], f"Failed to add movie. Status code: {response.status_code}"
    
    # Parse the response body
    try:
        response_data = response.json()
        print("Movie added successfully!")
        print(f"Response data: {json.dumps(response_data, indent=2)}")
    except json.JSONDecodeError:
        print("Response is not in JSON format.")

if __name__ == "__main__":
    print("Testing add movie functionality...")
    test_add_movie()