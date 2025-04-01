from sqlalchemy import Column, Integer, String, Date, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    UserId = Column(Integer, primary_key=True)
    history_entries = relationship("History", back_populates="user")
    playlists = relationship("Playlist", back_populates="user")

class Artist(Base):
    __tablename__ = 'Artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    tracks = relationship("Track", back_populates="artist")

class Genre(Base):
    __tablename__ = 'Genres'
    GenreId = Column(Integer, primary_key=True)
    GenreName = Column(String(255), nullable=False)

class Album(Base):
    __tablename__ = 'Albums'
    AlbumId = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Year = Column(Date)
    tracks = relationship("Track", back_populates="album")

class Track(Base):
    __tablename__ = 'Tracks'
    TrackId = Column(Integer, primary_key=True)
    Song = Column(String)
    Lyrics = Column(String)
    Name = Column(String(255))
    ArtistId = Column(Integer, ForeignKey('Artists.ArtistId', ondelete='CASCADE'))
    AlbumId = Column(Integer, ForeignKey('Albums.AlbumId', ondelete='CASCADE'))
    Year = Column(Date)
    Language = Column(String)
    Features = Column(ARRAY(float))
    SVDFeatures = Column(ARRAY(float))
    EmotionVector = Column(ARRAY(float))
    PhysicalSimilarTracksIds = Column(ARRAY(Integer))
    TextSimilarTracksIds = Column(ARRAY(Integer))
    CollaborationSimilarTracksIds = Column(ARRAY(Integer))

    artist = relationship("Artist", back_populates="tracks")
    album = relationship("Album", back_populates="tracks")
    history_entries = relationship("History", back_populates="track")
    playlist_tracks = relationship("PlaylistTracks", back_populates="track")

class Playlist(Base):
    __tablename__ = 'Playlists'
    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    UserId = Column(Integer, ForeignKey('Users.UserId', ondelete='CASCADE'))

    user = relationship("User", back_populates="playlists")
    playlist_tracks = relationship("PlaylistTracks", back_populates="playlist")

class History(Base):
    __tablename__ = 'History'
    HistoryId = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey('Users.UserId', ondelete='CASCADE'))
    TrackId = Column(Integer, ForeignKey('Tracks.TrackId', ondelete='CASCADE'))
    rating = Column(Integer, default=0)
    ListeningDate = Column(Date)

    user = relationship("User", back_populates="history_entries")
    track = relationship("Track", back_populates="history_entries")

class TrackGenres(Base):
    __tablename__ = 'TrackGenres'
    TrackId = Column(Integer, ForeignKey('Tracks.TrackId', ondelete='CASCADE'), primary_key=True)
    GenreId = Column(Integer, ForeignKey('Genres.GenreId', ondelete='CASCADE'), primary_key=True)

class AlbumGenres(Base):
    __tablename__ = 'AlbumGenres'
    AlbumId = Column(Integer, ForeignKey('Albums.AlbumId', ondelete='CASCADE'), primary_key=True)
    GenreId = Column(Integer, ForeignKey('Genres.GenreId', ondelete='CASCADE'), primary_key=True)
    __table_args__ = {'extend_existing': True}

class ArtistGenres(Base):
    __tablename__ = 'ArtistGenres'
    ArtistId = Column(Integer, ForeignKey('Artists.ArtistId', ondelete='CASCADE'), primary_key=True)
    GenreId = Column(Integer, ForeignKey('Genres.GenreId', ondelete='CASCADE'), primary_key=True)
    __table_args__ = {'extend_existing': True}

class AlbumArtists(Base):
    __tablename__ = 'AlbumArtists'
    AlbumId = Column(Integer, ForeignKey('Albums.AlbumId', ondelete='CASCADE'), primary_key=True)
    ArtistId = Column(Integer, ForeignKey('Artists.ArtistId', ondelete='CASCADE'), primary_key=True)
    __table_args__ = {'extend_existing': True}

class PlaylistTracks(Base):
    __tablename__ = 'PlaylistTracks'
    PlaylistId = Column(Integer, ForeignKey('Playlists.PlaylistId', ondelete='CASCADE'), primary_key=True)
    TrackId = Column(Integer, ForeignKey('Tracks.TrackId', ondelete='CASCADE'), primary_key=True)

    playlist = relationship("Playlist", back_populates="playlist_tracks")
    track = relationship("Track", back_populates="playlist_tracks")

class UserAlbums(Base):
    __tablename__ = 'UserAlbums'
    UserId = Column(Integer, ForeignKey('Users.UserId', ondelete='CASCADE'), primary_key=True)
    AlbumId = Column(Integer, ForeignKey('Albums.AlbumId', ondelete='CASCADE'), primary_key=True)
    __table_args__ = {'extend_existing': True}

class UserFavoriteArtists(Base):
    __tablename__ = 'UserFavoriteArtists'
    UserId = Column(Integer, ForeignKey('Users.UserId', ondelete='CASCADE'), primary_key=True)
    ArtistId = Column(Integer, ForeignKey('Artists.ArtistId', ondelete='CASCADE'), primary_key=True)
    __table_args__ = {'extend_existing': True}

class UserHistory(Base):
    __tablename__ = 'UserHistory'
    UserId = Column(Integer, ForeignKey('Users.UserId', ondelete='CASCADE'), primary_key=True)
    HistoryId = Column(Integer, ForeignKey('History.HistoryId', ondelete='CASCADE'), primary_key=True)
    __table_args__ = {'extend_existing': True}