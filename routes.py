from flask import render_template, request, jsonify
from  sqlalchemy.sql.expression import func, select
from models import Movie



def register_routes(app,db):
    @app.route('/')
    def home():
        return render_template('home.html')

    # Get a Random Movie
    @app.route('/movie', methods=['GET'])
    def movie():
        movie = Movie.query.order_by(func.random()).first()
        return render_template('movie.html', movie=movie)

    # Get 10 Random Movies
    @app.route('/movies', methods=['GET'])
    def top_movies():
        movies = Movie.query.order_by(func.random()).limit(10).all()
        return render_template('movies.html', movies=movies)
    
    @app.route('/add-movie', methods=['GET','POST'])
    def add_movie():
        if request.method == 'POST':
            data = request.form
            new_movie = Movie(
                poster_url=data.get('poster_url'),
                title=data.get('title'),
                year=int(data.get('year')),
                certificate=data.get('certificate'),
                genre=data.get('genre'),
                rating=float(data.get('rating')),
                metascore=float(data.get('metascore')),
                director=data.get('director'),
                cast=data.get('cast'),
                votes=int(data.get('votes').replace(',', '')),
                description=data.get('description'),
                review_count=int(data.get('review_count').replace(',', '')),
                review_title=data.get('review_title'),
                review=data.get('review')
            )
            db.session.add(new_movie)
            db.session.commit()
            return jsonify({'message': 'Movie added successfully!'}), 201
        # If GET request, render the add movie form
        if request.method == 'GET':
            # Render the add movie form
            return render_template('add_movie.html')
    
    @app.route('/manage-movies', methods=['GET'])
    def manage_movies():
        movies = Movie.query.all()
        return render_template('manage_movies.html', movies=movies)
    
    @app.route('/favourite-director', methods=['GET'])
    def favorite_director():
        favorite_director = db.session.query(
            Movie.director, func.count(Movie.director).label('count')
        ).group_by(Movie.director).order_by(func.count(Movie.director).desc()).first()
        favourite_dict = {
            'name': favorite_director[0],
            'count': favorite_director[1]
        }
        return render_template('favourite_director.html', director=favourite_dict)
    

        
    @app.route('/topmovies/<string:genre>', methods=['GET'])
    def top_movies_by_genre(genre):
        # Get the top 10 movies by genre
        movies = Movie.query.filter(Movie.genre.ilike(f"%{genre}%")).order_by(Movie.rating.desc()).limit(10).all()
        return render_template('top_movies_by_genre.html', movies=movies, genre=genre)

    @app.route('/list-genres', methods=['GET'])
    def list_genres():
        # Get all unique genres
        genres = db.session.query(Movie.genre).distinct().all()
        genre_list = []
        for genre in genres:
            if genre[0]:  # Check if the genre is not None or empty
                genre_list.extend([g.strip() for g in genre[0].split(',')])
        genre_list = list(set(genre_list))  # Remove duplicates
        return render_template('list_genres.html', genres=genre_list)

    # Seed Movies from CSV
    @app.route('/seed', methods=['POST'])
    def seed_movies():
        import csv
        with open('imdb-movies-dataset.csv', 'r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))
            for row in reader[:5000]:  # Limit to 1000 rows for seeding
                # Check if the movie already exists
                existing_movie = Movie.query.filter_by(title=row['Title'], year=int(row['Year'])).first()
                if existing_movie:
                    continue
                # Create a new movie instance
                new_movie = Movie(
                    id=reader.index(row) + 1,
                    poster_url=row['Poster'],
                    title=row['Title'],
                    year=int(row['Year']),
                    certificate=row['Certificate'],
                    genre=row['Genre'],
                    rating=float(row['Rating']) if row['Rating'] != '' else 0,
                    metascore=float(row['Metascore']) if row['Metascore'] != '' else 0,
                    director=row['Director'],
                    cast=row['Cast'],
                    votes=int(row['Votes'].replace(',', '')) if row['Votes'] != '' else 0,
                    description=row['Description'],
                    review_count=int(row['Review Count'].replace(',','')) if row['Review Count'] != '' else 0,
                    review_title=row['Review Title'],
                    review=row['Review']
                )
                db.session.add(new_movie)
            db.session.commit()
        return jsonify({'message': 'Movies seeded successfully!'}), 201
    
    