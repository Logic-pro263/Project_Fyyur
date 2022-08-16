from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

artist_genre = db.Table('artist_genre', 
    db.Column('genre_id', db.Integer, db.ForeignKey('genre_id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artist_id'), primary_key=True)
)

venue_genre = db.Table('venue_genre', 
    db.Column('genre_id', db.Integer, db.ForeignKey('genre_id'), primary_key=True),
    db.Column('venue_id', db.Integer, db.ForeignKey('venue_id'), primary_key=True)
)

class Venue(db.Model):  # Venue Model
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.relationship('Genre', secondary=venue_genre, backref=db.backref('venues'))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    websit_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean(), default=False)
    seeking_description = db.Column(db.Text)
    show = db.relationship('show', backref="show_venue", lazy=True, collection_class=list)
     


class Artist(db.Model):     #Artist Model
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.relationship('Genre', secondary=artist_genre, backref=db.backref('artists'))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean(), default=False)
    seeking_description = db.Column(db.Text)
    show = db.relationship('show', backref="show_artist", lazy=True, collection_class=list)


class Show(db.Model):       # Show Model
  __tablename__: 'show'
  id = db.Column(db.Integer, primary_key=True)
  Venue_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  Artist_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
  start_time = db.Column(db.DateTime(), nullable=False)


class Genre(db.Model):     # Genre Model
  __tablename__= 'genre'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(70), nullable=False)

