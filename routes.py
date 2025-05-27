from flask import render_template, request, jsonify
from  sqlalchemy.sql.expression import func, select
from models import Movie



def register_routes(app,db):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/movie', methods=['GET'])
    def movie():
        movie = Movie.query.order_by(func.random()).first()
        return render_template('movie.html', movie=movie)

    @app.route('/movies', methods=['GET'])
    def top_movies():
        movies = Movie.query.order_by(func.random()).limit(10).all()
        return render_template('movies.html', movies=movies)
    
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
    

    @app.route('/favourite-actor', methods=['GET'])
    def favorite_actor():
        all_actors = []

        movie_casts = db.session.query(Movie.cast).all()

        for movie_cast_tuple in movie_casts:
            movie_cast_string = movie_cast_tuple[0]
            if movie_cast_string:  # Check if the string is not None or empty
                actors = movie_cast_string.split(',')
                for actor in actors:
                    all_actors.append(actor.strip())  # Remove leading/trailing spaces

        from collections import Counter
        actor_counts = Counter(all_actors)

        if actor_counts:
            favorite_actor, count = actor_counts.most_common(1)[0]
        else:
            favorite_actor = "No actors found"
            count = 0

        favourite_dict = {
            'name': favorite_actor,
            'count': count
        }
        return render_template('favourite_actor.html', actor=favourite_dict)

        
    @app.route('/topmovies/<string:genre>', methods=['GET'])
    def top_movies_by_genre(genre):
        # Get the top 10 movies by genre
        movies = Movie.query.filter(Movie.genre.ilike(f"%{genre}%")).order_by(Movie.rating.desc()).limit(10).all()
        return render_template('top_movies_by_genre.html', movies=movies, genre=genre)

    @app.route('/list-genres', methods=['GET'])
    def list_genres():
        # Get all unique genres
        genres = db.session.query(Movie.genre).distinct().all()
        genre_list = [genre[0] for genre in genres]
        return render_template('list_genres.html', genres=genre_list)

    # Seed Movies from CSV
    @app.route('/seed', methods=['POST'])
    def seed_movies():
        import csv
        with open('imdb-movies-dataset.csv', 'r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))
            for row in reader[:100]:  # Limit to 100 rows for seeding
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
    
    