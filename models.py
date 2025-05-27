from main import db


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    poster_url = db.Column(db.String(500))
    title = db.Column(db.String(100), primary_key=True)
    year = db.Column(db.Integer)
    certificate = db.Column(db.String(10))
    genre = db.Column(db.String(100))
    rating = db.Column(db.Float)
    metascore = db.Column(db.Float)
    director = db.Column(db.String(100))
    cast = db.Column(db.String(500))
    votes = db.Column(db.Integer)
    description = db.Column(db.Text)
    review_count = db.Column(db.Integer)
    review_title = db.Column(db.String(200))
    review = db.Column(db.Text)

